"""
Public research preview stub for `benchmark_speed.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

def _read_json_if_exists(p):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _find_log_file(run_dir):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _infer_batch_size(run_dir):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _ensure_images_per_sec(df, run_dir):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _summarize_speed(df, run_dir, tail_epochs):
    """Returns (mean_imgps, median_imgps, max_imgps) over last tail_epochs rows that have images_per_sec."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def main():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
