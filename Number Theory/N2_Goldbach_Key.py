import math
def prime_check(natNum):
    flagVar=0
    w=math.ceil(natNum**0.5)
    for ii in range(1,w):
        nat=ii
        if (natNum%nat==0) and (nat!=1): 
            flagVar=1
    if flagVar==0:
        return True
    elif flagVar==1:
        return False

N=int(input("How many terms do you want in your sequence: "))
OddCompositeList=[]
PrimeList=[]

for ii in range(2,N+2):
    if (ii%2!=0) and (prime_check(ii)==False):
        OddCompositeList.append(ii)
#    elif prime_check(ii)==True:
#        PrimeList.append(ii)

#for OddCompNum in OddCompositeList:
#    for PrimeNum in PrimeList:
#        for Num in range(N):
#            if OddCompNum==PrimeNum+2*(Num**2):
#                GoldbachFlag=1
#    if GoldbachFlag==0:
#        print("%d is FALSE for Goldbach's conjecture."%(OddCompNum))
#        break
#    elif GoldbachFlag==1:
#       print("%d is true for Goldbach's conjecture."%(OddCompNum))
#    GoldbachFlag=0

for OddCompNum in OddCompositeList:
    GoldbachFlag=0
    upper=int((OddCompNum/2)**0.5)
    for Num in range(upper+1):
        if prime_check(OddCompNum-2*(Num**2))==True:
            GoldbachFlag=1
    if GoldbachFlag==0:
        print("%d is FALSE for Goldbach's conjecture."%(OddCompNum))
        break
    elif GoldbachFlag==1:
       print("%d is true for Goldbach's conjecture."%(OddCompNum))