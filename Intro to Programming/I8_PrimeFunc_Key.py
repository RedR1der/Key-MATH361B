def prime_check(natNum):
    flagVar=0 #A flag variable is established with the assumption that the input is a prime number until proven otherwise.
    for ii in range(1,natNum):
        nat=ii
        if (natNum%nat==0) and (nat!=1): #A for loop runs from 1 to natNum-1 and checks if any of those numbers are a multiple of natNum with the exception of 1.
            flagVar=1 #The flag variable's value is changed to establish that the input is composite.
    if flagVar==0: #0 stands for prime, meaning the statement "natNum is prime" is true.
        return "True"
    elif flagVar==1: #1 stands for composite, meaning the statement "natNum is prime" is false.
        return "False"
       
n=int(input("Enter the nth prime number you wish to find: ")) #A variable is created to find the nth term in a sequence of prime numbers.
nList=[]
count=2 #Due to the ranges for the for loops in prime_check and still wanting to make sure that the primality of 2 can be tested under its definition, the count starts at 2 instead of 1.

while len(nList) < n:
    if prime_check(count)=="True":
        nList.append(count)
    count+=1
    
if n==1:
    print("The largest prime number is 2. It is the 1st term.") #I had to hardcode for the case of a nList of length 1 because the while loop would always return an empty list.
else:
    print("The largest prime number is %d. It is the %dth term."%(max(nList),nList.index(max(nList))+1))