#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文字列の読み込み
str = input()
a = list(str)

s=0
t=0

for i in range(len(a)):
  if a[i] == "S":
    s=s+1
  else:
    if s > 0:
      s=s-1
    else:
      t=t+2
print(t)
