---
# applydict.py
Apply some function to keyword arguments

## description
Unless designate `func`, `func` is identity function

## usage

```python
# same as dict() function
>>> apply_dict(apple=5, orrange=10)
{'apple': 5, 'orrange': 10}

# apply some function to dict
>>> apply_dict(func=lambda x**2, apple=5, orrange=10)
{'apple': 25, 'orrange': 100}
```


---
# caldict.py

## CalDict
Caluculatable dictionary with operator

## description
* Caluculatable dictionary with operator
* python dictionary enhancement
* inherit of UserDict

## usage

```python
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
```


---
# pandas_tools.py
pandas useful tools

## less
* df.less(): Append `df.head()` with `df.tail()`
* df.mirror(): Append reverse DataFrame

## mirror
Append reverse DataFrame

## w2db, db2w, v2db, db2v
convert dB and Watt


---
# graph_tools.py
python graph tools

## fine_ticks()
fine_ticks(): divide list from min to max

### usage

```python
>>> xticks = np.arange(181)
>>> fine_ticks(xticks,30)
array([   0.,   30.,   60.,   90.,  120.,  150.,  180.])
>>> fine_ticks(xticks,60)
array([   0.,   60.,  120.,  180.])
>>> fine_ticks(xticks,90)
array([   0.,   90.,  180.])
```
