# coding:utf-8

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。 x.capitalize()
'''


L = ['adam', 'LISA', 'barT']

def format(x):
    if isinstance(x,str) == False:
        raise "Input content not string, please transfer the string type."
    else:
        return x.capitalize()

print map(format, L)