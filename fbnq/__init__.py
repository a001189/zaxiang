#!/usr/local/bin python
# -*-coding:utf-8-*-
'''

'''
import time
from functools import wraps


def cache(func):
    caches = {}
    @wraps(func)
    def wrapper(num):
        if num in caches:
            pass
        else:
            caches[num] = func(num)
        return caches[num]

    return wrapper

@cache
def fb(num):
    if num <= 2:
        res = 1
    else:
        res = fb(num - 1) + fb(num - 2)
    return res


def fb2(num):
    if num <= 2:
        res = 1
    else:
        res = fb2(num - 1) + fb2(num - 2)
    return res


def usetime(fb, num):
    ts = time.time()
    print("斐波那契额数列第%d位结果为:%d" % (num, fb(num)))
    td = time.time()
    print("菲波那切函数%s用时：%s" % (fb.__name__, str(td - ts)))


if __name__ == "__main__":
    usetime(fb, 36)