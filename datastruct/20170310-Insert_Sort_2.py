#!/usr/bin/env python
# encoding=utf-8

source = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]
def insert_sort():  
    for index in range(1,len(source)):
        current_val = source[index]     #先记下来每次大循环走到的第几个元素的值
        position = index

        while position > 0 and source[position-1] > current_val: 
            #当前元素的左边的紧靠的元素比它大,
            #要把左边的元素一个一个的往右移一位,
            #给当前这个值插入到左边挪一个位置出来
            source[position] = source[position-1] #把左边的一个元素往右移一位
            position -= 1 #只一次左移只能把当前元素一个位置 ,还得继续左移只到此元素放到排序好的列表的适当位置 为止

        source[position] = current_val #已经找到了左边排序好的列表里不小于current_val的元素的位置,把current_val放在这里
        print(source)

"""
[77, 92, 67, 8, 6, 84, 55, 85, 43, 67]
[67, 77, 92, 8, 6, 84, 55, 85, 43, 67]
[8, 67, 77, 92, 6, 84, 55, 85, 43, 67]
[6, 8, 67, 77, 92, 84, 55, 85, 43, 67]
[6, 8, 67, 77, 84, 92, 55, 85, 43, 67]
[6, 8, 55, 67, 77, 84, 92, 85, 43, 67]
[6, 8, 55, 67, 77, 84, 85, 92, 43, 67]
[6, 8, 43, 55, 67, 77, 84, 85, 92, 67]
[6, 8, 43, 55, 67, 67, 77, 84, 85, 92]
"""

if __name__ == "__main__":
    insert_sort()
