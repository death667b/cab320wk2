# -*- coding: utf-8 -*-

import itertools

xvec = list(itertools.permutations([10,20,30,40,50,60,70,80]))

aa= ((x,y,z,a,b,c) 
    for x,y,z,_,_,_,_,_ in xvec
    if x == 20
    if y == 10
    if z == 30
    for a,b,c,_,_,_,_,_ in xvec
    if a == 10
    if b == z
    if c == x
    )

for a in aa:
    print(a)