"""
Public research preview stub for `eval_robust.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

def parse_frac(value):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _safe_get_model(dataset, model_name, num_classes):
    """Handle both possible get_model signatures:"""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _select_state_dict(ckpt):
    """Prefer model_state_dict when available."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _needs_wrap(sd):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _build_model(args, num_classes, sd):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def local_pgd_attack(model, x, y, eps, alpha, steps, p, random_start):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def eval_clean(model, loader, device):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def eval_pgd(model, loader, device, eps, alpha, steps, p):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def main():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
