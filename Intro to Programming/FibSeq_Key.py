# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:24:10 2019

@author: Olivia
"""
myList=[]
F0=int(input("Enter your first term: "))
F1=int(input("Enter your second term: "))
N=int(input("How many terms do you want in your sequence? "))
myList.append(F0)
myList.append(F1)
placeholder=0

for ii in range(2,N):
    myList.append(myList[ii-1]+myList[ii-2])
for terms in range(1,N-1):
    if (((myList[terms]**2)-(myList[terms-1])*(myList[terms+1]))==((-1)**(ii-1))):
        placeholder=1
if placeholder==1:
    print("Cassini's identity applies here.")
else:
    print("Cassini's identity does not apply here.")

print("Here are the last ten terms of the sequence:",myList[-10:N])

