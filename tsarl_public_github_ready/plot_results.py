"""
Public research preview stub for `plot_results.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

def _read_csv(path):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _maybe_read_json(path):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _find_epoch_col(df):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _find_first(df, candidates):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _find_best_pgd_rob_col(df):
    """Prefer the robust column with the largest PGD steps:"""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _infer_batch_size_from_run_dir(run_dir):
    """Try to infer batch_size from config.json or run_args.json located next to the CSV."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _get_throughput_series(df, run_dir):
    """Return (label, series) where series is either images/sec or sec/iter depending on availability."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _save_plot(path):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def main():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
