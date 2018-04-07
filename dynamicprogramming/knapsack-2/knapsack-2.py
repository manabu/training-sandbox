#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, max_w = [int(i) for i in input().split()]#print(n, max_w)

v = []
w = []
for j in range(n):
    value,weight=[int(i) for i in input().split()]
    v.append(value)
    w.append(weight)

dp = [[0 for i in range(max_w+1)] for j in range(n+1)]

for i in range(n):
    for cw in range(max_w+1):
        if cw >= w[i]:
            dp[i+1][cw] = max(dp[i][cw-w[i]]+v[i], dp[i][cw])
        else:
            dp[i+1][cw] = dp[i][cw]
print(dp[n][max_w])