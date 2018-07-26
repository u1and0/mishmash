#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pandas useful tools
* df.less(): Append `df.head()` with `df.tail()`
* df.mirror(): Append reverse DataFrame
"""
import pandas as pd


def _less(self, n=10):
    """Append `df.head()` with `df.tail()`"""
    return self.head(n // 2).append(self.tail(n // 2))


pd.DataFrame.less = _less
pd.Series.less = _less


def _mirror(self):
    """Append reverse DataFrame"""
    return self.append(self[-2::-1], ignore_index=True)


pd.DataFrame.mirror = _mirror
pd.Series.mirror = _mirror
