"""
Public research preview stub for `tsarl/projection.py`.

This file preserves the public-facing module layout, API names, and high-level
research structure for TSARL while withholding core implementation details
until formal publication.
"""

PUBLIC_RELEASE = True
IMPLEMENTATION_STATUS = 'redacted'

class LinfProjectSTE:
    """Straight-through estimator for Linf projection:"""
    def forward(ctx, delta, eps):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

    def backward(ctx, grad_output):
        raise NotImplementedError(
            'Core method withheld from public preview pending paper publication.'
        )

def project_lp(delta, eps, p):
    """Global projection onto the Lp ball with radius eps."""
    raise NotImplementedError(
        'Core function withheld from public preview pending paper publication.'
    )
