#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 数値読み込み
a,b = [int(i) for i in input().split()]


if a <= 0 and b >=0:
  print("Zero")
elif a<0 and b<0 and (a-b)%2==0:
  print("Negative")
else:
  print("Positive")
