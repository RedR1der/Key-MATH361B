def Divisor_Finder(n):
    divList=[]
    for m in range(1,n):
        if n % m == 0:
            divList.append(m)
    return divList

print(Divisor_Finder(100))