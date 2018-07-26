#!/usr/bin/env python3
"""
# CalDict
* Caluculatable dictionary with operator
* python dictionary enhancement
* inherit of UserDict
"""
from collections import UserDict


class CalDict(UserDict):
    """Caluculatable dictionary with operator
    usage:
        # calculate
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic + 5
        {'a': 6, 'b': 10, 'c': 20}
        >>> cdic - 5
        {'a': -4, 'b': 0, 'c': 10}
        >>> cdic * 5
        {'a': 5, 'b': 25, 'c': 75}
        >>> cdic / 5
        {'a': 0.2, 'b': 1.0, 'c': 3.0}
        >>> cdic // 5
        {'a': 0, 'b': 1, 'c': 3}
        >>> cdic % 5
        {'a': 1, 'b': 0, 'c': 0}
        >>> cdic ** 5
        {'a': 1, 'b': 3125, 'c': 759375}
        >>> -cdic
        {'a': -1, 'b': -5, 'c': -15}
        >>> cdic > 0
        True
        >>> cdic > 1
        False
        >>> -cdic <= -1
        True

        # self calculate
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic -= 5
        >>> cdic
        {'a': -4, 'b': 0, 'c': 10}

        # reverse caluculate
        >>> cdic = CalDict(a=2, b=5, c=10)
        >>> 2 / cdic
        {'a': 1.0, 'b': 0.4, 'c': 0.2}

        # element add
        >>> cdic = CalDict(a=1, b=-1, c=15)
        >>> bdic = CalDict(a=1, b=1, c=1)
        >>> cdic += bdic
        >>> cdic  # all key
        {'a': 2, 'b': 0, 'c': 16}
        >>> cdic + {'a': 5, 'c':-5}  # particular keys
        {'a': 7, 'b': 0, 'c': 11}

        # slice
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic['a']  # normal slice
        1
        >>> cdic['a','c']  # multiple slice
        {'a': 1, 'c': 15}
        >>> list(cdic['a','c'].values())  # get list values
        [1, 15]

        # function apply
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic.apply(sum)
        21
        >>> cdic.apply(lambda x: x**2)
        {'a': 1, 'b': 25, 'c': 225}
        >>> cdic.apply(lambda x,y,z: x*y*z, 10, 0.5)
        {'a': 5.0, 'b': 25.0, 'c': 75.0}
        >>> cdic.apply([max,min])
        {'max': 15, 'min': 1}

        # stats
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic.max()
        15
        >>> cdic.min()
        1
        >>> cdic.sum()
        21
        >>> cdic.mean()
        7.0
        >>> cdic.sort(reverse=True)
        {'c': 15, 'b': 5, 'a': 1}
    """

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def __add__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] + value[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: v + value for k, v in self.items()})

    def __radd__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] + self[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: value + v for k, v in self.items()})

    def __sub__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] - value[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: v - value for k, v in self.items()})

    def __rsub__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] - self[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: value - v for k, v in self.items()})

    def __mul__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] * value[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: v * value for k, v in self.items()})

    def __rmul__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] * self[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: value * v for k, v in self.items()})

    def __truediv__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] / value[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: v / value for k, v in self.items()})

    def __rtruediv__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] / self[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: value / v for k, v in self.items()})

    def __floordiv__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] // value[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: v // value for k, v in self.items()})

    def __rfloordiv__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] // self[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: value // v for k, v in self.items()})

    def __mod__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] % value[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: v % value for k, v in self.items()})

    def __rmod__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] % self[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: value % v for k, v in self.items()})

    def __pow__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i]**value[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: v**value for k, v in self.items()})

    def __rpow__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i]**self[i] for i in value.keys()})
            return dic
        except AttributeError:
            return CalDict(**{k: value**v for k, v in self.items()})

    def __neg__(self):
        return CalDict(**{k: -v for k, v in self.items()})

    def __gt__(self, value):
        return all(i > value for i in self.values())

    def __lt__(self, value):
        return all(i < value for i in self.values())

    def __ge__(self, value):
        return all(i >= value for i in self.values())

    def __le__(self, value):
        return all(i <= value for i in self.values())

    def __getitem__(self, key):
        if len(key) < 2:
            return self.data[key]
        return CalDict(**{i: self.data[i] for i in key})

    def apply(self, func, *args, **kwargs):
        """Using one or more operations over keys
        usage:
            cdic = CalDict(a=1, b=5, c=15)
            cdic.apply(sum)
            21
            cdic.apply(lambda x: x**2)
            {'a': 1, 'b': 25, 'c': 225}
            cdic.apply(lambda x,y,z: x*y*z, 10, 0.5)
            {'a': 5.0, 'b': 25.0, 'c': 75.0}
            cdic.apply([max,min])
            {'max': 15, 'min': 1}
        """
        if isinstance(func, (list, tuple)):
            return CalDict(
                **{f.__name__: self.apply(f, *args, **kwargs)
                   for f in func})
        else:
            try:
                return CalDict(
                    **{k: func(v, *args, **kwargs)
                       for k, v in self.items()})
            except (ValueError, AttributeError, TypeError):
                return func(self.values(), *args, **kwargs)

    def max(self):
        """return max of values"""
        return self.apply(max)

    def min(self):
        """return min of values"""
        return self.apply(min)

    def sum(self):
        """return sum of values"""
        return self.apply(sum)

    def mean(self):
        """return mean of values"""
        return self.apply(sum) / len(self)

    def sort(self, key=lambda x: x[1], reverse=False):
        """sorted by values"""
        return CalDict(**dict(sorted(self.items(), key=key, reverse=reverse)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
