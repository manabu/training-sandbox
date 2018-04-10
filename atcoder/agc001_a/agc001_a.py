#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [競プロ等におけるpython3の標準入力 - Qiita](https://qiita.com/zenrshon/items/c4f3849552348b3dbe67)

# 数値の数の読み込み
n = int(input())
# 数値読み込み
a = [int(i) for i in input().split()]
a.sort(reverse=True)
print(sum(a[1::2]))