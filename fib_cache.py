#!/usr/bin/env python
# coding=utf-8

import sys
#from functools import wraps

def cache(func):
    '''i am in cache'''
    caches={}

    #@wraps(func)
    def wrap(*args):
        if args not in caches:
            caches[args] = func(*args)

        #print caches
        print func.__name__
        print func.__doc__
        return caches[args]
    return wrap


@cache
def fib(n):
    '''i am in fib'''
    assert n > 0, 'invalid n'

    if n < 3:
        return 1
    
    return (fib(n-1) + fib(n-2))


if __name__ == '__main__':
    for i in range(len(sys.argv)):
        print sys.argv[i]
    
    print fib(int(sys.argv[1]))
