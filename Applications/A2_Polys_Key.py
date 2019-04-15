#Let p(x)=(4*x**4)-(3*x**3)-(9*x)+8
def evalPol(coeff,x,exp):
    return coeff*x**exp
def ptplyderive(coeff,x,exp):
    return coeff*exp*(x**(exp-1))
def plyderive(coeff,exp):
    if exp == 0:
        return 'flag' #If the exponent of an element in the polynomial is 0, that means its coefficient is a constant and will disappear when differentiated; in this case, the function returns a string 'flag' which is used to idenitfy which elements in the list derivedcoefficients needs to be removed 
    return coeff*exp
def plyintegrate(coefflist,a,b,explist):
    alist=[] #This list will represent the integral of the polynomial evaluated at x=a
    blist=[] #This list will represent the integral of the polynomial evaluated at x=b
    for polyparts in range(len(coefflist)):
        alist.append((coefflist[polyparts]/(explist[polyparts]+1))*a**(explist[polyparts]+1))
        blist.append((coefflist[polyparts]/(explist[polyparts]+1))*b**(explist[polyparts]+1))
    return sum(blist)-sum(alist)

x=int(input("Input a value for x: "))
b=int(input("Enter the upper bounds of your definite integral: "))
a=int(input("Enter the lower bounds of your definite integral: "))
coefficients=[4,-3,0,-9,8] #This is a list of coefficients that coincides with the list [x**n,x**(n-1),....,x**0]; for example, the coefficient 4 is the coefficent of x**4
dp=[] #This list will represent each 'part' of the derivative of p
exponents=[] #This list stores exponents of the polynomial from the highest exponent to the lowest
derivedcoefficients=[] #This list will store the coefficients of the derivatives
evaluatedpolynomial=[] #This list will store each 'part' of a polynomial evaluated at a given point x

for exponent in range(len(coefficients)-1,-1,-1): #The range of the for loop represents the exponents of x in descending order; for example, given a polynomial p=x**n+x**(n-1)+....+x**0 means the index of the for loop will go in order i=n,n-1,....,0
    dp.append(ptplyderive(coefficients[len(coefficients)-1-exponent],x,exponent)) #The relation between the indices of the coefficients list on their respective exponents is index = highest index - exponent
    derivedcoefficients.append(plyderive(coefficients[len(coefficients)-1-exponent],exponent))
    evaluatedpolynomial.append(evalPol(coefficients[len(coefficients)-1-exponent],x,exponent))
    exponents.append(exponent)
print("The polynomial evaluated at a given point p(%d) = %d" %(x,sum(evaluatedpolynomial)))
print("The derivative of p(%d) is p'(%d) = %d" % (x,x,sum(dp)))
for ii in derivedcoefficients:
    if ii == 'flag':
        derivedcoefficients.remove(ii)
print("The cofficients of p'(x) are from highest exponent to lowest exponent",derivedcoefficients)
print("The integral of p(x) from point x = %d to x = %d is %f" %(a,b,plyintegrate(coefficients,a,b,exponents)))

    