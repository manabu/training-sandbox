#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
b = [int(i) for i in input().split()]
b.sort(reverse=True)
a=b
alicelist=a[0::2]
alice=sum(alicelist)
boblist=a[1::2]
bob=sum(boblist)
print(alice-bob)

