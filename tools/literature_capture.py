#!/usr/bin/env python3
"""检索公开学术来源并把可下载的 PDF 保存到 Raw sources。

脚本只使用 Python 标准库，不依赖 API key。GPT Researcher 或人工筛选的
结果可以通过 --from-results 以 JSON 数组（或 {"results": [...]}）传入。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


USER_AGENT = "song-second-brain-literature-capture/1.0"
SEMANTIC_SCHOLAR_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
ARXIV_URL = "https://export.arxiv.org/api/query"
TIMEOUT_SECONDS = 30


def _request(url: str, accept: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": accept},
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return response.read()


def _request_json(url: str) -> dict[str, Any]:
    return json.loads(_request(url, "application/json"))


def _normalise_authors(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        authors: list[str] = []
        for item in value:
            if isinstance(item, str):
                authors.append(item)
            elif isinstance(item, dict) and item.get("name"):
                authors.append(str(item["name"]))
        return authors
    return [str(value)]


def _normalise_year(value: Any) -> int | None:
    if value is None or value == "":
        return None
    match = re.search(r"\d{4}", str(value))
    return int(match.group()) if match else None


def _normalise_record(raw: dict[str, Any], source_hint: str | None = None) -> dict[str, Any]:
    open_access = raw.get("openAccessPdf")
    if isinstance(open_access, dict):
        open_access_url = open_access.get("url")
    else:
        open_access_url = None

    title = str(raw.get("title") or "").strip()
    if not title:
        raise ValueError("结果缺少 title 字段")

    source_url = (
        raw.get("source_url")
        or raw.get("sourceUrl")
        or raw.get("url")
        or raw.get("link")
        or ""
    )
    pdf_url = raw.get("pdf_url") or raw.get("pdfUrl") or raw.get("pdf") or open_access_url or ""
    return {
        "title": title,
        "authors": _normalise_authors(raw.get("authors")),
        "year": _normalise_year(raw.get("year") or raw.get("published")),
        "source": str(raw.get("source") or source_hint or "external"),
        "source_url": str(source_url).strip(),
        "pdf_url": str(pdf_url).strip(),
    }


def _search_semantic_scholar(query: str, limit: int) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode(
        {
            "query": query,
            "limit": limit,
            "fields": "title,authors,year,url,openAccessPdf",
        }
    )
    payload = _request_json(f"{SEMANTIC_SCHOLAR_URL}?{params}")
    return [_normalise_record(item, "semantic-scholar") for item in payload.get("data", [])]


def _search_arxiv(query: str, limit: int) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode(
        {
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": limit,
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
    )
    root = ET.fromstring(_request(f"{ARXIV_URL}?{params}", "application/atom+xml"))
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    records: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", namespace):
        title = " ".join((entry.findtext("atom:title", "", namespace)).split())
        source_url = entry.findtext("atom:id", "", namespace).strip()
        pdf_url = ""
        for link in entry.findall("atom:link", namespace):
            if link.attrib.get("title") == "pdf":
                pdf_url = link.attrib.get("href", "")
                break
        if not pdf_url and source_url:
            pdf_url = source_url.replace("http://arxiv.org/abs/", "https://arxiv.org/pdf/") + ".pdf"
        records.append(
            _normalise_record(
                {
                    "title": title,
                    "authors": [
                        author.findtext("atom:name", "", namespace).strip()
                        for author in entry.findall("atom:author", namespace)
                    ],
                    "published": entry.findtext("atom:published", "", namespace),
                    "source_url": source_url,
                    "pdf_url": pdf_url,
                },
                "arXiv",
            )
        )
    return records


def _record_key(record: dict[str, Any]) -> str:
    source_url = record["source_url"].lower().strip()
    if source_url:
        return f"url:{source_url}"
    return f"title:{re.sub(r'\W+', ' ', record['title'].lower()).strip()}"


def _collect_records(
    query: str | None,
    limit: int,
    result_file: Path | None,
) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    if query:
        for name, search in (("Semantic Scholar", _search_semantic_scholar), ("arXiv", _search_arxiv)):
            try:
                records.extend(search(query, limit))
            except (
                urllib.error.HTTPError,
                urllib.error.URLError,
                TimeoutError,
                ET.ParseError,
                json.JSONDecodeError,
            ) as exc:
                message = f"{name}: {exc}"
                errors.append(message)
                print(f"[search-error] {message}", file=sys.stderr)
    if result_file:
        payload = json.loads(result_file.read_text(encoding="utf-8"))
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        if not isinstance(items, list):
            raise ValueError("--from-results 必须是 JSON 数组或包含 results 数组的对象")
        records.extend(_normalise_record(item) for item in items)

    unique: list[dict[str, Any]] = []
    seen: set[str] = set()
    for record in records:
        key = _record_key(record)
        if key not in seen:
            unique.append(record)
            seen.add(key)
    return unique[:limit], errors


def _safe_project_name(project: str) -> str:
    value = project.strip()
    if not value or value in {".", ".."} or any(char in value for char in '\\/:*?"<>|'):
        raise ValueError("项目名只能是普通文件夹名称，不能包含路径分隔符或保留字符")
    return value


def _safe_filename(title: str) -> str:
    value = re.sub(r"[<>:\"/\\|?*\x00-\x1f]", "-", title).strip().strip(".")
    value = re.sub(r"\s+", " ", value)
    return (value[:120] or "untitled") + ".pdf"


def _existing_filename(previous: list[dict[str, Any]], record: dict[str, Any]) -> str | None:
    key = _record_key(record)
    for item in previous:
        if _record_key(item) == key and item.get("local_filename"):
            return str(item["local_filename"])
    return None


def _download(record: dict[str, Any], pdf_dir: Path, filename: str) -> tuple[str, str | None]:
    if not record["pdf_url"]:
        return "no-pdf-url", None
    target = pdf_dir / filename
    if target.exists():
        return "exists", None
    try:
        data = _request(record["pdf_url"], "application/pdf")
        if not data.startswith(b"%PDF"):
            raise ValueError("响应不是 PDF 文件")
        target.write_bytes(data)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as exc:
        return "error", str(exc)
    return "downloaded", None


def run(args: argparse.Namespace) -> int:
    project = _safe_project_name(args.project)
    if not args.query and not args.from_results:
        raise ValueError("至少提供 --query 或 --from-results")
    if args.limit < 1:
        raise ValueError("--limit 必须大于 0")
    if args.year_from and args.year_to and args.year_from > args.year_to:
        raise ValueError("--year-from 不能晚于 --year-to")

    records, search_errors = _collect_records(args.query, args.limit, args.from_results)
    records = [
        item
        for item in records
        if (args.year_from is None or item["year"] is None or item["year"] >= args.year_from)
        and (args.year_to is None or item["year"] is None or item["year"] <= args.year_to)
    ]
    if not records:
        raise RuntimeError("没有找到符合条件的文献；可调整关键词，或使用 --from-results 提供结果")

    download_root = args.download_root.resolve()
    project_dir = (download_root / project).resolve()
    if download_root not in project_dir.parents:
        raise ValueError("下载路径必须位于 --download-root 下")
    pdf_dir = project_dir / "PDF原件"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = project_dir / "download_manifest.json"
    previous: list[dict[str, Any]] = []
    if manifest_path.exists():
        old_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        previous = old_manifest.get("papers", [])

    used_names: set[str] = set()
    papers: list[dict[str, Any]] = []
    for record in records:
        filename = _existing_filename(previous, record) or _safe_filename(record["title"])
        stem = Path(filename).stem
        suffix = Path(filename).suffix
        counter = 2
        while filename in used_names:
            filename = f"{stem}-{counter}{suffix}"
            counter += 1
        used_names.add(filename)
        status, error = _download(record, pdf_dir, filename)
        paper = {**record, "local_filename": filename, "local_path": f"PDF原件/{filename}", "status": status}
        if error:
            paper["error"] = error
        papers.append(paper)
        print(f"[{status}] {record['title']} -> {filename}")

    manifest = {
        "project": project,
        "query": args.query or "",
        "focus": args.focus or "",
        "year_from": args.year_from,
        "year_to": args.year_to,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "download_root": str(download_root),
        "search_errors": search_errors,
        "papers": papers,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"清单已写入：{manifest_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="搜索学术文献并下载 PDF，生成 download_manifest.json")
    parser.add_argument("--query", help="学术检索主题，建议使用英文")
    parser.add_argument("--focus", help="本次关注重点，例如计量模型、实证方法或数据来源")
    parser.add_argument("--project", required=True, help="项目子文件夹名称")
    parser.add_argument("--limit", type=int, default=5, help="最多保留的文献数量（默认 5）")
    parser.add_argument("--year-from", type=int, help="最早年份（含）")
    parser.add_argument("--year-to", type=int, help="最晚年份（含）")
    parser.add_argument(
        "--download-root",
        type=Path,
        default=Path("raw") / "参考文献",
        help="下载根目录（默认 raw/参考文献）",
    )
    parser.add_argument("--from-results", type=Path, help="外部结果 JSON 文件")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return run(args)
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
