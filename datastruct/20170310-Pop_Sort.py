#encoding=utf-8
#Bub sort
data_set = [ 9,1,22,31,45,3,6,2,11 ]
 
loop_count = 0
for j in range(len(data_set)):              #遍数。
    for i in range(len(data_set) - j- 1):   #每一遍都要把当前最大值排到当前最后一个。
        # -1 是因为每次比对的都 是i 与i +1,不减1的话,最后一次对比会超出list 获取范围,
        # -j是因为,每一次大loop就代表排序好了一个最大值,放在了列表最后面,下次loop就不用再运算已经排序好了的值 了
        if data_set[i] > data_set[i+1]: #switch
            #tmp = data_set[i]
            #data_set[i] = data_set[i+1]
            #data_set[i+1] = tmp
            data_set[i],data_set[i+1] = data_set[i+1],data_set[i]   #利用很Python的语句使代码有趣~
        loop_count +=1
    print(data_set)
print(data_set)
print("loop times", loop_count)
