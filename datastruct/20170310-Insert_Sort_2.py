

source = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]
  
  
for index in range(1,len(source)):
    current_val = source[index] #先记下来每次大循环走到的第几个元素的值
    position = index
  
    while position > 0 and source[position-1] > current_val: #当前元素的左边的紧靠的元素比它大,要把左边的元素一个一个的往右移一位,给当前这个值插入到左边挪一个位置出来
        source[position] = source[position-1] #把左边的一个元素往右移一位
        position -= 1 #只一次左移只能把当前元素一个位置 ,还得继续左移只到此元素放到排序好的列表的适当位置 为止
  
    source[position] = current_val #已经找到了左边排序好的列表里不小于current_val的元素的位置,把current_val放在这里
    print(source)

	
	"""结果：

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


#更容易理解的版本

data_set = [ 9,1,22,9,31,-5,45,3,6,2,11 ]
for i in range(len(data_set)):
    #position  = i
    while i > 0 and data_set[i] < data_set[i-1]:# 右边小于左边相邻的值
        tmp = data_set[i]
        data_set[i] = data_set[i-1]
        data_set[i-1] = tmp
        i -= 1
    # position  = i
    # while position > 0 and data_set[position] < data_set[position-1]:# 右边小于左边相邻的值
    #     tmp = data_set[position]
    #     data_set[position] = data_set[position-1]
    #     data_set[position-1] = tmp
    #     position -= 1

#插入排序