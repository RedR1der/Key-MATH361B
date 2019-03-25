#a and b are zero divisors if a*b=nk+r such that r=0
m=int(input("Enter your m value for the set Z_m: "))
Z_m=[]
ZeroDivisors=[]

for rs in range(1,m): #starting from 1 b/c we want to check all non-zero elements of Z_m
    Z_m.append(rs)

for elements in Z_m:
    for ii in range(1,m): #starting from 1 b/c we want to check all non-zero elements of Z_m
        if (elements*ii) % m == 0:
            print(elements,"and",ii,"are zero divisors of",m)
            ZeroDivisors.append(elements)

for divs in ZeroDivisors:
    while ZeroDivisors.count(divs) > 1:
        ZeroDivisors.remove(divs)
        
print()
print(m,"has in total",len(ZeroDivisors),"zero divisors:")
print(ZeroDivisors)