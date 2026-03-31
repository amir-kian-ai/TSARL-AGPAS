"""
Public research preview stub for `tsarl/accelerated_train.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

def save_json(path, obj):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def parse_frac(value):
    """Accepts: 0.03137 or 8/255 (quoted or unquoted)."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _construct_cfg(cls, **kwargs):
    """Create config object passing only supported fields."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def set_seed(seed):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def local_pgd_attack(model, x, y, eps, alpha, steps, p, random_start):
    """PGD implementation that does NOT change model mode."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def safe_pgd_adv(model, x, y, eps, alpha, steps, p):
    """Generates PGD adversarial examples while:"""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def eval_clean(model, loader, device, channels_last):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def eval_pgd(model, loader, device, eps, alpha, steps, p, channels_last):
    """PGD eval must allow gradients for attack, but not for final accuracy forward."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def main():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
