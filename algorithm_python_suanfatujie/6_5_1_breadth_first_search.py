#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/3 06:33'


'''
6-5-1 广度优先搜索算法
算法图解 P85-90
'''

# 使用deque来创建一个双端队列
from collections import deque

# P85 散列表将键映射到值
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
# print(graph)


# 判断一个人是否是芒果销售商
def person_is_seller(name):
    # print(name[-1])
    return name[-1] == 'm'  # 检查这个人的名字是否以m结尾，是则是芒果销售商


# P90 广度优先算法的最终代码
def search(name):
    search_queue = deque()  # 创建一个队列 deque 即双端队列,是一种具有队列和栈的性质的数据结构。双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。
    search_queue += graph[name]  # 将你的所有邻居都加入到这个搜索队列中 graph["you"]是一个数组
    searched = []    # 数组用于记录检查过的人

    while search_queue:     # 只要队列不为空
        person = search_queue.popleft()      # 就取出其中的第一个人(从最左边弹出)
        if person not in searched:       # 仅当此人没被检查过时才检查
            if person_is_seller(person):     # 检查这个人是否是芒果销售商
                print("%s is a mango seller!" % person)    # print mango seller
                return True
            else:
                search_queue += graph[person]     # 不是芒果经销商，则将这个人的朋友都加入搜索队列
                searched.append(person)      # 将此人标记为已检查过的
    print("You friends are not mango seller.")
    return False     # 说明没人是芒果销售商


if __name__ == '__main__':
    # search("bob")
    search("you")

