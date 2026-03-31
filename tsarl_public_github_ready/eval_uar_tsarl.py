"""
Public research preview stub for `eval_uar_tsarl.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

def ensure_parent_dir(path):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def load_checkpoint_flex(path, map_location):
    """Flexible checkpoint loader."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def normalize_norm_name(p):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def margin(logits, y):
    """Margin:"""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def clean_eval(model, loader, device, num_batches):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def pgd_eval(model, loader, device, eps, alpha, steps, p, num_batches):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def autoattack_eval(model, loader, device, eps, p, num_batches):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def parse_args():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def main():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
