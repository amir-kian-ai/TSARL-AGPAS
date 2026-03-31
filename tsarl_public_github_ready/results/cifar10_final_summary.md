# CIFAR-10 public result summary

## Robustness evaluation

| Method | H | Nat. | PGD-10 | PGD-20 | PGD-50 | AA |
|---|---:|---:|---:|---:|---:|---:|
| TSARL | 4 | 90.60 | 58.06 | 55.09 | 52.29 | 49.60 |

## Efficiency and evaluation setup

| Item | Value |
|---|---|
| Throughput | 4.5k-6.1k img/s |
| Speedup vs. PGD-50 | 9.5x |
| Threat model | Linf, eps = 8/255 |
| PGD step size | alpha = 2/255 |
| Final projection | Applied in all runs |
