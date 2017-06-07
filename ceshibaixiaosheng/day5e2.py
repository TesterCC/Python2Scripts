# coding: utf-8

def foo(s):
    try:
        int_s = int(s)
    except ZeroDivisionError, e:
        raise ValueError("Division cannot equal zero!")

def bar(s):
    try:
        result = foo(s)*2
    except SystemError, e:
        raise ValueError("Division is error!")

def main():
    try:
        bar(0)
    except SystemError, e:
        print "Handle SystemError"
    except ZeroDivisionError, e:
        print "Handle ZeroDivisionError"
    except StandardError, e:
        print "Handle StandardError"
    except ValueError, e:
        print "Handle ValueError"
    finally:
        print "Finally!"

# 调用主函数
if __name__ == '__main__':
    main()
