from dataclasses import dataclass

"""
Public research preview stub for `tsarl/data.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

@dataclass
class DataConfig:
    """Redacted public stub."""
    dataset: str = 'cifar10'
    data_dir: str = './data'
    batch_size: int = 128
    num_workers: int = 4
    pin_memory: bool = True

def get_dataset_stats(dataset):
    """Returns (mean, std) tuples for model-side normalization."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _canon_dataset(dataset):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _maybe_strong_cifar100_aug():
    """CIFAR-100 often benefits from slightly stronger augmentation for generalization."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _cifar_transforms(dataset):
    """Returns (train_tf, test_tf) for CIFAR datasets, keeping tensors in [0,1]."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def _imagenet_transforms():
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

def get_loaders(cfg):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
