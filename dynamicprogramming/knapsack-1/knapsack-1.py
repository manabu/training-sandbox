#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [競プロ等におけるpython3の標準入力 - Qiita](https://qiita.com/zenrshon/items/c4f3849552348b3dbe67)

# 数値の数の読み込み
n = int(input())
# 数値読み込み
list = [int(input()) for i in range(n)]
# 初期化
dp=[0 for i in range(n+1)]

dp[0]=0

for i in range(n):
    dp[i+1]=max(dp[i], dp[i]+list[i])
print("%d\n"% dp[n])