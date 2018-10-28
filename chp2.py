# -*- coding: utf-8 -*-
# @Time : 2018/10/24 22:36
# @Author : csk
# @FileName: chp2.py
# @log:

import os
from collections import namedtuple

# sequences 分为flat和container两种
# container存储reference , flat存储value
# 也可以分为 mutable(list, bytearray, array, collections), immutable(tuple, str, bytes)

# 请注意区别 container, iterable, sized -- sequence -- mutable sequence之间的关系, 每个都是实现了特定的方法，方法组
# 而具有了某些性质的

symbols = 'sasa11s'
codes = [ord(s) for s in symbols]
print(codes)
# 列表推导式仅仅用于生成列表


# 强大的generator
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
print('%s %s' %(c, s) for c in colors for s in sizes)

# tuples as records
# tuples unpacking
# 这可以用来解锁最后一个文件名, _用作占位符号

path = 'a/b/c/d/e.csv'
_, filename = os.path.split(path)
print(filename)
*_, filename = path.split('/')
print(_, filename)

# nested tuple unpacking
# namedTuple 是一个类 or 元类, 和词典不同, attribute统统存放在 class 里面
City = namedtuple('city', 'name country population coordinates') # class name, filed names
tokyo = City('Tokyo', 'JP', 36.933, (35.75, 129.990911)) #

LatLong = namedtuple('latlong', 'lat long')
delhi_data = ('ncr', 'in', 21.99, LatLong(1, 2))
delhi = City._make(delhi_data) # 从迭代器生成City
print(delhi)
print(delhi._asdict()) # 生词有序的词典

## 聊聊切片
## 为何切片不带最后一个元素?
# 容易计算个数
# 容易开始和结尾的分离
a = [1, 2, 3]
a[:3] = [5] # 用于元素的修改
print(a)

# [] * 3 对于可修改元素的赋值，这是很危险的，因为会指到同一个数组！！
a = [[0.5]] * 3
a[0].append(1)
print(a)

# += 不是一个原子化的操作, 可能在修改之后才抛出错误
a = (1, 2, [3])
a[2] *= 2
print(a)