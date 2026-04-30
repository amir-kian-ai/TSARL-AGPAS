# TSARL: Public Research Preview

This repository is a **public research preview** for **TSARL (Temporal-Spatial Adaptive Robust Learning)** and related experimental variants developed for adversarially robust learning under norm-bounded threat models.

## Why this repository is public but partially redacted

The associated manuscript is not yet published. To establish an early public timestamp and document the project structure, this repository exposes:

- the module layout,
- script names,
- public API names,
- evaluation protocol summary,
- result snapshots,
- dependency summary, and
- high-level research intent.

The **core training logic, optimizer details, structured perturbation planner internals, and exact implementation recipes are intentionally withheld** until formal publication or a later open-source release.

## What is included

- Public stubs for training and evaluation entry points
- Public stubs for TSARL/AGPAS-related modules
- A result snapshot for CIFAR-10, CIFAR-100, ImageNet
- Minimal repository metadata for citation and authorship tracking

## What is intentionally withheld

- Full runnable training code
- Exact inner-loop generation logic
- Full loss construction and scheduler details
- Complete experiment automation
- Reproduction-ready checkpoints and private logs

## Repository structure

```text
.
├── assets/
│   └── cifar10_results_table.png
├── results/
│   ├── cifar10_final_summary.csv
│   └── cifar10_final_summary.md
├── tsarl/
│   ├── agpas.py
│   ├── agpas_optimized.py
│   ├── agpas_uar.py
│   ├── data.py
│   ├── projection.py
│   └── ...
├── README.md
├── CITATION.cff
├── NOTICE.md
├── PUBLIC_RELEASE_POLICY.md
└── requirements-public.txt
```

## Result snapshot

Main CIFAR-10 result reported in this preview:

| Method | H | Nat. | PGD-10 | PGD-20 | PGD-50 | AA |
|---|---:|---:|---:|---:|---:|---:|
| TSARL | 4 | 90.60 | 58.06 | 55.09 | 52.29 | 49.60 |

Additional setup summary:

| Item | Value |
|---|---|
| Throughput | 6080 img/s |
| Speedup vs. PGD-50 | 9.5x |
| Threat model | Linf, eps = 8/255 |
| PGD step size | alpha = 2/255 |
| Final projection | Applied in all runs |

See `assets/cifar10_results_table.png` and `results/` for the public summary artifacts.

## Usage note

This preview is **not intended to be reproduction-ready**. Any missing implementation is deliberate.

## Citation

Please cite the associated manuscript or contact the author for collaboration inquiries before using unpublished details beyond what is visible here.
