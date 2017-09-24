#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/24 22:48'

'''
Python基础 2-2.4 应用:猜拳游戏
'''

import random

player = input('请输入：剪刀(0)  石头(1)  布(2):')

player = int(player)

computer = random.randint(0, 2)

# 用来进行测试
print('player=%d,computer=%d', (player, computer))

if ((player == 0) and (computer == 2)) or ((player == 1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print("You are win!")
elif player == computer:
    print("Tie, try again please.")
else:
    print("You are failed. Try agin!")