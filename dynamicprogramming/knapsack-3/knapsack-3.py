#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# 数値の数の読み込み
n = int(input())
# 数値読み込み
list = [int(input()) for i in range(n)]
# 目的の数 A
A = int(input())
# 初期化
dp = [[0 for i in range(A+1)] for j in range(n+1)]

for i in range(n):
    for cw in range(A+1):
        if cw == dp[i][cw]+list[i]:
            dp[i+1][cw] = list[i]
result = False
for i in range(A):
    if dp[n][i] != 0:
        result = True
        break
if result:
    print("YES")
else:
    print("NO")