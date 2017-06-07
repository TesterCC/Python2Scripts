# coding: utf-8

class GrandFather:
    age = 70

class Father(GrandFather):
    pass

class Son(Father):
    pass

if __name__ == '__main__':
    print GrandFather.age , Father.age, Son.age # 70,70,70
    Son.age = 20
    print GrandFather.age , Father.age, Son.age # 70,70,20
    Father.age = 50
    print GrandFather.age , Father.age, Son.age # 70,50,20