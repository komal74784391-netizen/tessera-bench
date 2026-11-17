# tessera-bench

Benchmark harness for **TESSERA: A Reproducible Suite for Tabular Robustness Evaluation**, published in JEMS 2024.

## Repository contents

- `harness/` — suite runner and report generator
- `suites/` — suite definitions used in the paper
- `results/` — baseline results released with the paper
- `cli_interface.json` — machine-readable interface of the harness CLI

## Quick start

```bash
python harness/run_suite.py --suite suites/core.yaml
```

## Citation

> A. Diaz, P. Nwosu. TESSERA: A Reproducible Suite for Tabular Robustness Evaluation. JEMS 2024.
