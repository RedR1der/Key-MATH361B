import numpy as np

def prime_check(natNum):
    flagVar=0
    for ii in range(1,natNum):
        nat=ii
        if (natNum%nat==0) and (nat!=1): 
            flagVar=1 
    if flagVar==0:
        return True
    elif flagVar==1:
        return False

P=int(input("Enter the upper limit for finding the largest prime number: "))
PrimeNums=[]

for ps in range(P):
    if prime_check(ps+2) == True:
        PrimeNums.append(ps+2)
LenQuad=np.zeros(len(PrimeNums))
count=np.array([PrimeNums,LenQuad])
neg_one=np.array([PrimeNums,LenQuad])

col1="p"
col2="Number of Quadratic Residues in Z_p" 
col3="Is -1 a Quadratic Residue? (1 means yes, 0 means no)"
print("%-5s %-5s %-5s" % (col1, col2, col3))

for i in range(len(PrimeNums)):
    Answer=0
    QuadRes=[]
    for ii in range(PrimeNums[i]): #Check if lower bound should be 1 or 0
        QuadRes.append((ii**2) % PrimeNums[i])
        if ((ii**2)+1) % PrimeNums[i] == 0:#if ((ii**2)-(PrimeNums[i]-1)) % PrimeNums[i] == 0:#
            Answer=1
    for quads in QuadRes:
        while QuadRes.count(quads) > 1:
            QuadRes.remove(quads)
    print("Quads for",PrimeNums[i],"are",QuadRes)
    count[1,i] = len(QuadRes) #REMINDER: Row 0 is the prime numbers and row 1 is the number of quads
    neg_one[1,i] = Answer
    print("%-5d %-5d %31d" % (count[0,i], count[1,i], neg_one[1,i]))