#!/usr/bin/env python
# coding=utf-8

#Min heap by yangli

def min_heap_fix_down(array, i, n):
    temp = array[i]
    j = 2*i + 1

    while j < n :

        if j+1 < n and array[j] > array[j+1]:
            j = j+1 #j record the smaller one of child

        if temp <= array[j]:
            break #in right order, nothing todo

        #else, set array i
        array[i] = array[j]

        i = j 
        j = 2*i+1

    array[i] = temp
    print array

#del on number in MimHeap
def min_deap_del_num(a,n):
    a[0],a[n-1] = a[n-1],a[0]
    min_heap_fix_down(a,0,n-1)

#build up min-heap
def buildup_min_heap(a,n):
    for i in range(n//2 -1, -1,-1):
        min_heap_fix_down(a,i,n-1)

#sort heap
def min_heap_sort(a,n):
    for i in range(n-1,0,-1):#range: include head but not end
        a[i],a[0] = a[0],a[i]
        min_heap_fix_down(a,0,i-1)

if __name__ == "__main__" :
    a = [16,9,21,3,13,14,23,6,4,11,3,15,99,8,22] #len 15
    print a
    buildup_min_heap(a,len(a))
    print a
    print "==="
    min_heap_sort(a,len(a))
    print "==="
    print a
