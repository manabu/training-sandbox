#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 数値読み込み
n = int(input())
s = input()
t = input()

res=len(s)
while(len(s)>0):
  if s==t:
    break
  else:
    res=res+1
    s=s[1:]
    t=t[:-1]
print(res)
