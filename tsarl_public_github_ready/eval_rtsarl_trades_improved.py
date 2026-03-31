"""
Public research preview stub for `eval_rtsarl_trades_improved.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

def build_model_from_rb(rb_model_name, dataset, threat_model):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def load_checkpoint_flex(path, map_location):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def normalize_state_dict_keys(sd):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def safe_load_model(model, ckpt_path, map_location, strict):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def margin(logits, y):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def local_pgd_attack(model, x, y, eps, alpha, steps, p, random_start):
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

def collect_subset(loader, num_batches):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def autoattack_eval(model, loader, device, eps, norm, batch_size, num_batches):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def main():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
