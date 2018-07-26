#!/usr/bin/env python3
"""python graph tools"""

import numpy as np


def fine_ticks(ticks, div):
    """
    descriptions:
        divide list from min to max
    usage:
        >>> xticks = np.arange(181)
        >>> fine_ticks(xticks,30)
        array([   0.,   30.,   60.,   90.,  120.,  150.,  180.])
        >>> fine_ticks(xticks,60)
        array([   0.,   60.,  120.,  180.])
        >>> fine_ticks(xticks,90)
        array([   0.,   90.,  180.])
    """
    tick_min = min(ticks)
    tick_max = max(ticks)
    return np.linspace(tick_min, tick_max, (tick_max - tick_min) / div + 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
