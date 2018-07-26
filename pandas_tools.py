#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pandas useful tools
* df.less(): Append `df.head()` with `df.tail()`
* df.mirror(): Append reverse DataFrame
"""
import numpy as np
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


def w2db(x):
    """mW -> dB"""
    return 10 * np.log10(x)


def db2w(x):
    """
    dB -> mW
    `df.db2w()` or `db2w(df)`

    ```python
    # TEST
    se = pd.Series(np.arange(10))
    db = se.w2db()
    df = pd.DataFrame({'dBm': db,
                       'watt': db.db2w()})
    print(df)
    ```
    """
    return np.power(10, x / 10)


def v2db(x):
    """V -> dB"""
    return 20 * np.log10(x)


def db2v(x):
    """dB -> V"""
    return np.power(10, x / 20)


def a2comp(mag, arg):
    """
    mag(大きさ)とarg(角度)を引数に、複素数表示で返す。
    引数:
        mag: magnitude
        arg: argument
    戻り値: 複素数表示
    """
    return mag * (np.cos(np.radians(arg)) + np.sin(np.radians(arg)) * 1j)


TYPES = (pd.DataFrame, pd.Series)
NAMES = ('less', 'mirror', 'w2db', 'db2w', 'v2db', 'db2v')
FUNCS = (_less, _mirror, w2db, db2w, v2db, db2v)
for t in TYPES:
    for n, f in zip(NAMES, FUNCS):
        setattr(t, n, f)
