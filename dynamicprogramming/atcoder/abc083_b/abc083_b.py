#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 読み込み
n,a,b=[int(i) for i in input().split()]
#
result=0
for i in range(n+1):
    val = 0
    temp = i
    while temp > 0:
        val = val + (temp%10)
        temp=int(temp/10)
    if a <= val and val <=b:
        result=result+i
print(result)