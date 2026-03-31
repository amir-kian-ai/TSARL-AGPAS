"""
Public research preview stub for `tsarl/meters.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

class AvgMeter:
    """Tracks running average of a scalar."""
    def __init__(self):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

    def reset(self):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

    def update(self, value, k):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

    def avg(self):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

class Timer:
    """Reliable timer for GPU code."""
    def __init__(self, use_cuda_sync):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

    def start(self):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

    def stop(self):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )
