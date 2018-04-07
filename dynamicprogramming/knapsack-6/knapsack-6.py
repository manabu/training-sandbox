#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# 大きな数

BIGNUM = 100009;

# 数値の数の読み込み
n = int(input())
# 個数K
k = int(input())
# 数値読み込み
list = [int(input()) for i in range(n)]
# 目的の数 A
A = int(input())
# 初期化
dp = [[BIGNUM for i in range(A+1)] for j in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(A+1):
        if j >= list[i]:
            dp[i+1][j]=min(dp[i][j-list[i]]+1,dp[i][j])
        else:
            dp[i+1][j]=dp[i][j]
if dp[n][A]!=BIGNUM and dp[n][A] <= k:
    print("YES")
else:
    print("NO")