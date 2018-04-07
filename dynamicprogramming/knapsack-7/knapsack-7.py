#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# 数値の数の読み込み
n = int(input())
# 数値読み込み
items = [int(input()) for i in range(n)]
m =  [int(input()) for i in range(n)]
# 目的の数 A
A = int(input())
##
# 初期化
dp = [[0 for i in range(A+1)] for j in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(A+1):
        flag=True
        if j % 50 !=0:
            continue
        for mm in range(1,m[i]+1):
            val = items[i]*mm
            if j >= val and (j==val or dp[i][j-val]>0):
                dp[i+1][j]=dp[i+1][j]+dp[i][j-val]
                flag=False
        if flag:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=dp[i+1][j]+dp[i][j]

print(dp[n][A])
