from functools import reduce

def list_operation(n, way):
    '''
    n = 创建几个列表进行操作
    way = 对这几个列表进行什么样的操作
    '''
    list_create = [[] for i in range(n)]  # 创建n维列表
    for i in range(n):
        list_create[i] = input().split(',')
    num = sorted([set(i) for i in list_create])   # 对列表元素重新排序，并使列表可以操作

    return way(num)

def union(num):
    return reduce(lambda x, y: x | y,num)         # 集合的并集操作

def interaction(num):
    return reduce(lambda x, y: x & y, num)        # 集合的交集操作

def difference(num):
    return reduce(lambda x, y: x - y,num)         # 集合的差集操作

print(list_operation(2, interaction))
