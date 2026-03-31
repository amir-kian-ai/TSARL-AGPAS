"""
Public research preview stub for `tsarl/normalize.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

def get_stats(dataset):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )

class NormalizeLayer:
    """Redacted public stub."""
    def __init__(self, mean, std):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

    def forward(self, x):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

class NormalizedModel:
    """Redacted public stub."""
    def __init__(self, base, dataset):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

    def forward(self, x):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

def wrap_model(base, dataset):
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
