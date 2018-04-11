#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 数値読み込み
a,b,c = [int(i) for i in input().split()]

if a*b*c % 2 == 0:
  print(0)
else:
  d = [a,b,c]
  d.sort()
  print(d[0]*d[1])
