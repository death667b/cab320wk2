# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:05:12 2018

@author: n5372828


a. ok..
b. u-turn
c. -c will rotate the commands counter-clockwise
   n-c will do the same as -c
d. 0 or n
e. all values are a u-turn
f. c1 = 1
   c2 = 2
   c3 = 3

***

function explore
    if [destination] then return node
    if [child = 0] then return null
    while [child nodes > 0]
        add node to queue(this is a SET)
        child nodes - 1
    explore[pop node from queue]    

"""

# 
def ch4():
    C = [1,0,2,2,0,2,0,2,3,2,0,2,1,0,1]
    D = [4,1,4,3,1,3,1,3,4,3,1,3,3,1,3]
    
    changed = True
    
    while changed:
        k = len(C)
        changed = False
        for i in list(range(1,k-1)):
            print('k = ', k, ' and i = ', i)
            if not C[i]%D[i]==C[i]:
                changed = True
                print(C)
                print(D)
                C[i-1] = C[i-1] + C[i+1]
                del D[i],  D[i+1], C[i], C[i+1]
                break
            
def ans():
    C = [1,0,2,2,0,2,0,2,3,2,0,2,1,0,1]
    D = [4,1,4,3,1,3,1,3,4,3,1,3,3,1,3]
    
    while True:
        k =len(C)
        for i in list(range(1,k-1)):
            if C[i] % D[i] == 0:
                C[i] = (C[i-1] + C[i+1]) % D[i-1]
                del C[i+1], C[i-1], D[i+1], D[i]
                break
                
        if all(c % D[C.index(c)] != 0 for c in C):
            return C             

if __name__ == "__main__":
    C = ans()
    print(C)

