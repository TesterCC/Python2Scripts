# coding:utf-8

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

if __name__ == '__main__':
    add_end()
    add_end()
    add_end()