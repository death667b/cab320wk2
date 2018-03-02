
# Code for CAB320  wk02 prac

# Adapted from Peter Norvig



# last modified by f.maire@qut.edu.au on 2017/02/27


# For compatibility with Python 2.7
# A future statement is a directive to the compiler that a particular module 
# should be compiled using syntax or semantics that will be available in a 
# specified future release of Python.
# The future statement is intended to ease migration to future versions of 
# Python that introduce incompatible changes to the language. It allows use 
# of the new features on a per-module basis before the release in which the 
# feature becomes standard.
from __future__ import print_function
from __future__ import division



import itertools, time

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h2-h1) == 1

def zebra_puzzle():
    '''
        ??  What is returned by this function?

        Uncomment the commented constraints to perform
        the search with all the constraints of the puzzle

    '''
    houses = first, _, middle, _, _ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses)) #1
    genExp = ((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in orderings
            if imright(green, ivory)                #6
            for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
            if Norwegian == first                   #10
            if Englishman == red                    #2
            if nextto(Norwegian, blue)              #15
            for (dog, snails, fox, horse, ZEBRA) in orderings
            if Spaniard == dog                      #3
            for (coffee, tea, milk, oj, WATER) in orderings
            if milk == middle                       #9
            if Ukranian == tea                      #5
            if coffee == green                      #4
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if OldGold == snails                    #7
            if Kools == yellow                      #8
            if nextto(Chesterfields, fox)           #11
            if nextto(Kools, horse)                 #12
            if LuckyStrike == oj                    #13
            if Japanese == Parliaments              #14
            )
    return genExp

## - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    g = zebra_puzzle()
    
    t0 = time.clock()
    (w,z) = next(g)
    t1 = time.clock()
    
    print ('w, z = {0},{1}'.format(w,z))
    print ('Search took {0} seconds'.format(t1-t0))
    
    print ('a generator object is returned')
    print ('next(g) will iterate of the generator - in this case there is only one response')

