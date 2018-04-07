#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# 大きな数

BIGNUM = 1000000009;
# 数値の数の読み込み
n = int(input())
# 数値読み込み
items = [int(input()) for i in range(n)]
m =  [int(input()) for i in range(n)]
# 目的の数 A
A = int(input())
##
# nl = []
# index = 0
# for i in range(n):
#     for j in range(1,m[i]+1):
#         nl.append(list[i]*j)
 
# print(n)
print(items)
print(m)
# print(nl)
# print(A)
# #sys.exit(0)
# n = len(nl)
# print(n)
#sys.exit()
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
                print("----%d,%d,val=%d,j-val=%d,i=%d,j=%d" % (items[i],mm,val,j-val,i,j))
                #print(items[i]*mm)
                dp[i+1][j]=dp[i+1][j]+(dp[i][j-val])
                print(dp[i+1][j])
                flag=False
                #break
        if flag:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=dp[i+1][j]+dp[i][j]

for i in range(n+1):
    aaa=[]
    for j in range(0,A+1,50):
        aaa.append(dp[i][j])
    #aaa.append(dp[i])
    print(aaa)
print(dp[n][A])
