#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文字列の読み込み
str = input()
a = list(set(str))
if len(a)==4:
    print("Yes")
elif len(a)%2==1:
    print("No")
else:
    if ('N' in a and 'S' in a ) or ('W' in a and 'E' in a ):
        print("Yes")
    else:
        print("No")