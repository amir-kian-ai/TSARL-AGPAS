"""
Public research preview stub for `train_robust_tsarl.py`.

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

def set_seed(seed):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def save_json(path, obj):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _safe_get_model(dataset, model_name, num_classes):
    """Handle both possible get_model signatures:"""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _make_agpas(args):
    """Handle multiple AGPASConfig field variants across repo versions."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _schedule_linear(epoch, start_epoch, ramp_epochs, v0, v1):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _schedule_int(epoch, start_epoch, ramp_epochs, v0, v1):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def local_pgd_attack(model, x, y, eps, alpha, steps, p, random_start):
    """Fallback PGD (works without tsarl.pgd)."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def generate_adv(model, agpas, x, y, use_pgd, eps, alpha, steps, p, attack_bn_eval):
    """Generate adversarial examples in FP32."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def eval_clean(model, loader, device):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def eval_pgd(model, loader, device, eps, alpha, steps, p):
    """Robust eval requires gradients for attack generation."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def main():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
