#a and b are multiplicative inverses if a*b=nk+r such that r=1
m=int(input("Enter your m value for the set Z_m: "))
Z_m=[]
MInverses=[]

for rs in range(1,m): #starting from 1 b/c we want to check all non-zero elements of Z_m
    Z_m.append(rs)

for elements in Z_m:
    for ii in range(1,m): #starting from 1 b/c we want to check all non-zero elements of Z_m
        if (elements*ii-1) % m == 0:
            print(elements,"and",ii,"are multiplicative inverses of",m)
            MInverses.append(elements)
            
for invs in MInverses:
    while MInverses.count(invs) > 1:
        MInverses.remove(invs)
        
print()
print(m,"has in total",len(MInverses),"multiplicative inverses:")
print(MInverses)