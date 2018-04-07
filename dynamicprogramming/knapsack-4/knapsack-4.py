#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# 割る数

MOD = 1000000009;

# 数値の数の読み込み
n = int(input())
# 数値読み込み
list = [int(input()) for i in range(n)]
# 目的の数 A
A = int(input())
# 初期化
dp = [[0 for i in range(A+1)] for j in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(A+1):
        if j >= list[i]:
            dp[i+1][j]=(dp[i][j-list[i]]+dp[i][j]) % MOD
        else:
            dp[i+1][j]=dp[i][j]
print(dp[n][A])