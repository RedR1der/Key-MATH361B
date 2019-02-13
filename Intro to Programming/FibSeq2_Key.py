# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:56:21 2019

@author: Olivia
"""

N=int(input("How many terms do you want in your Fibonacci sequence? "))
m=int(input("Enter a value for m to see if any Fibonacci terms are its multiples: "))
Multiples_of_m=[]

#----------------------------Fibonacci Sequence--------------------------------
Fibonacci=[0,1]
for ii in range(2,N):
    Fibonacci.append(Fibonacci[ii-1]+Fibonacci[ii-2])
#------------------------------------------------------------------------------

for n in Fibonacci:
    if n % m==0:
        Multiples_of_m.append(n)
 
print("The number of terms that are divisible by m is %d."%(len(Multiples_of_m)))
print()       
print("The following Fibonacci terms are divisible by m: ",Multiples_of_m)