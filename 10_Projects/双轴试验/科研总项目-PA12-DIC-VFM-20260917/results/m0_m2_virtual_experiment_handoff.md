# M0–M2 synthetic FE–VFM handoff

## Boundary

All values below belong to a generic synthetic virtual experiment. They are neither real
PA12 measurements nor literature/calibrated PA12 parameters.

## Noiseless recovery

UX and EQ were used for identification; R05 was completely held out.

| Model | Truth                         | Identified                              | Max relative parameter error | R05 virtual-work error |
| ----- | ----------------------------- | --------------------------------------- | ---------------------------: | ---------------------: |
| M0    | `sigma0=5 MPa, H=25 MPa`      | `5.000071 MPa, 25.000013 MPa`           |                    `1.42e-5` |              `6.00e-6` |
| M1    | `sigma0=5 MPa, Q=9 MPa, b=35` | `4.999210 MPa, 9.002070 MPa, 34.991799` |                    `2.34e-4` |              `2.12e-6` |
| M2    | `K=18 MPa, eps0=0.01, n=0.18` | `17.997591 MPa, 0.00998715, 0.1799439`  |                    `1.29e-3` |              `1.92e-5` |

All nine canonical FE datasets have 23 frames and 692 CPS4R elements. Direct Abaqus
truth-field external/internal virtual-work closure is between `8.67e-7` and `1.97e-5`.

## Actual commands

```powershell
& $py generate_inputs.py
& 'D:\SIMULIA\Commands\abaqus.bat' job=<job> input=<input.inp> interactive
& 'D:\SIMULIA\Commands\abaqus.bat' python extract_odb_history.py <job.odb> <dataset.npz>
& $py identifier.py --truth-model <M0|M1|M2> --train <UX.npz> <EQ.npz> --holdout <R05.npz> --output <result.json> --starts 1 --jobs 12
& $py -m unittest discover -s tests -v
```

## Gate handoff

- Gate 3: synthetic nonlinear FE truth and VFM work balance passed; real PA12 remains blocked.
- Gate 4: synthetic M0–M2 noiseless recovery passed; real PA12 remains blocked.
- Gate 8: synthetic held-out R05 prediction passed; it does not establish experimental generalization.
- Gates 5–7 remain open. Deterministic CLI interfaces now exist for multistart, strain/force
  noise, wrong-model fitting, and fixed seeds.
- Next action: run the prescribed multistart/noise/model-form matrix, then FIM/conditioning and
  path-information analysis. Do not connect real PA12 until field schema, synchronization, and
  four-channel boundary-force contracts are closed.
