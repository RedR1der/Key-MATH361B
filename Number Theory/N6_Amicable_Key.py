def Divisor_Finder(n):
    divList=[]
    for m in range(1,n):
        if n % m == 0:
            divList.append(m)
    return divList

N = int(input("What will be the upper bound? "))
for B in range(2,N):
    A = sum(Divisor_Finder(B))
    if sum(Divisor_Finder(A)) == B:
        print(A,"and",B,"are an amicable pair.")