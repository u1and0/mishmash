#!/usr/bin/env python3
"""Apply some function to keyword arguments"""


def apply_dict(func=lambda x: x, **kwargs):
    """Apply some function to keyword arguments

    description:
        Unless designate `func`, `func` is identity function

    usage:
        # same as dict() function
        >>> apply_dict(apple=5, orrange=10)
        {'apple': 5, 'orrange': 10}

        # apply some function to dict
        >>> apply_dict(func=lambda x**2, apple=5, orrange=10)
        {'apple': 25, 'orrange': 100}
    """
    return {k: func(v) for k, v in kwargs.items()}
