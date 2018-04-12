#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数値の読み込み
x,y = [int(i) for i in input().split()]

res = 0


if abs(y) > abs(x):
    # |x| < |y|
    if x < 0:
        res = res + 1
    if y < 0:
        res = res + 1
    res = res + (abs(y)-abs(x))
else :
    # x > y
    if x > 0:
        res = res + 1
    if y > 0:
        res = res + 1
    res = res + (abs(x)-abs(y))


print(res)