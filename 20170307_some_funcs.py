#!/usr/bin/env python
# coding=utf-8



def pr_eth(*args):
    for count, name in enumerate(args):
        print "{count}: {name}".format(count = count,name =name)

#pr_eth("ren","gou","hou")

def fib(n):
    a = 1
    b = 1
    for i in range(n-1):
        print i
        a,b = b,a+b
        print a,b
    return a

#fib(5)

import time
def fun1():
    for i in range(1,10):
        print
        for j in range(1,i+1):
            print "%d*%d=%d"%(i,j,i*j),
#fun1()

def time_test():
    print
    time.sleep(1)
    print time.time(),"time.time()"
    print time.localtime(time.time())
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#time_test()

def func11():
    f1 = 1
    f2 = 1
    print f1
    for i in range(21):
        f1,f2 = f2,f1+f2
        print f1

#func11()
#打印素数
#isinstance(value, type)
#地板除影响结果，结果都是int， 还是老实用取余吧,
#即使不是地板除，那整除结果也是一个float，还是不行
import math
def func12():
    count = 0
    for dog in range(100,200):
        leap = 1
        sp_dog = int(math.sqrt(dog+1))
        #print 'sp_dog',sp_dog
        for j in range(2,sp_dog+1):
            if (dog%j == 0):
            #if isinstance(dog//j,int ):
                leap = 0
                break
            else:
                continue

        if leap == 1:
            count += 1
            print dog

    print "total %d leap number"%count
    return

func12()



#打印水仙花数
#地板除？？？？
def func13():
    count = 0
    for dog in range(101,1000):#101--999
        b = dog/100
        s = (dog - b*100)/10
        g = (dog - b*100 - s*10)
        #print "%d%d%d"%(b,s,g)
        if b*b*b + s*s*s + g*g*g == dog:
            count += 1
            print count,": ",dog
    return

#func13()

#分解质因数
def func14():
    
    
    
    return
func14()


