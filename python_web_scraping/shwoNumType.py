#!/usr/bin/env python
# coding:utf-8


'''
python网络爬虫实战--胡松涛
P7-8
Linux下C++ style
'''


class ShowNumType(object):

    # 显示Python的数字类型

    def __init__(self):
        self.showInt()
        self.showLong()
        self.showFloat()
        self.showComplex()

    def showInt(self):
        print(u"#######显示整型#######")
        print(u"十进制整数")
        print("%-20d,%-20d,%-20d" % (-10000, 0, 1000))
        print(u"二进制整数")
        print("%-20s,%-20s,%-20s" % (bin(-10000), bin(0), bin(1000)))
        print(u"八进制整数")
        print("%-20s,%-20s,%-20s" % (oct(-10000), oct(0), oct(1000)))
        print(u"十六进制整数")
        print("%-20s,%-20s,%-20s" % (hex(-10000), hex(0), hex(1000)))

    def showLong(self):
        print(u"#######显示长整型#######")
        print(u"十进制整数")
        print("%-20Ld,%-20Ld,%-20Ld" % (-10000000000, 0, 10000000000))
        print(u"二进制整数")
        print("%-20s,%-20s,%-20s" % (bin(-10000000000), bin(0), bin(10000000000)))
        print(u"八进制整数")
        print("%-20s,%-20s,%-20s" % (oct(-10000000000), oct(0), oct(10000000000)))
        print(u"十六进制整数")
        print("%-20s,%-20s,%-20s" % (hex(-10000000000), hex(0), hex(10000000000)))

    def showFloat(self):
        print(u"#######显示浮点型#######")
        print("%-20.10f,%-20.10f,%-20.10f" % (-100.01, 0, 100.01))

    def showComplex(self):
        print(u"#######显示复数型#######")
        print(u"变量赋值复数 var = 3 + 4j")
        var = 3 + 4j
        print(u"var的实部是：%d\tvar的虚部是：%d" % (var.real, var.imag))


if __name__ == '__main__':
    showNum = ShowNumType()


