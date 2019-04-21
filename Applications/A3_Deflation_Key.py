def reverselist(mylist):
    rlist=[]
    for i in range(len(mylist)-1,-1,-1):
        rlist.append(mylist[i])
    return rlist      

def addpolys(coefficients1,coefficients2):
    #NOTE: The exponents should go from lowest to highest in numerical order for this function to work
    polysum = [] #This list will represent the coefficients of the sum of two polynomials going from lowest corresponding exponent to highest
    cosmall=[] #Indicates the coefficients of the polynomial with the smaller degree
    colarge=[] #Indicates the coefficients of the polynomial with the larger degree
    lengthind = 0 #Indicates the length of the polynomial with the larger degree
    if len(coefficients1) > len(coefficients2):
        lengthind = len(coefficients1)
        colarge = coefficients1
        cosmall = coefficients2
    elif len(coefficients2) >= len(coefficients1):
        lengthind = len(coefficients2)
        colarge = coefficients2
        cosmall = coefficients1
    for extraexpo in range(len(cosmall),len(colarge)): #This for loop will add extra coefficients and exponent indices to the polynomial with the smaller degree; note that the range goes from 1 higher than the degree of the smaller polynomial to the degree of larger polynomial
        cosmall.append(0)
    for i in range(lengthind):
        polysum.append(colarge[i]+cosmall[i])
    while (polysum[len(polysum)-1] == 0) and (len(polysum)-1 != 0): #This while loop cleans up the polynomial so that if the coefficient of the highest exponent is 0 and the highest exponent is not 0, it will be removed from the list
        polysum.pop(len(polysum)-1)
    return polysum

def subtractpolys(coefficients1,coefficients2):
    #NOTE 1: The exponents should go from lowest to highest in order for this function to work
    polydifference = [] #This list will represent the coefficients of the difference of two polynomials going from lowest corresponding exponent to highest; note that this function returns poly2 - poly1
    cosmall=[] #Indicates the coefficients of the polynomial with the smaller degree
    colarge=[] #Indicates the coefficients of the polynomial with the larger degree
    lengthind = 0 #Indicates the length of the polynomial with the larger degree
    if len(coefficients1) > len(coefficients2):
        lengthind = len(coefficients1)
        cosmall = coefficients2
        colarge = coefficients1
    elif len(coefficients2) >= len(coefficients1):
        #NOTE 2: This is set up so that if degree(poly2)=degree(poly1), the coefficients of poly1 are subtracted from that of poly2 or in other words, the function returns the polynomial for poly2 - poly1
        lengthind = len(coefficients2)
        cosmall = coefficients1
        colarge = coefficients2
    for extraexpo in range(len(cosmall),len(colarge)): #This for loop will add extra coefficients and exponent indices to the polynomial with the smaller degree; note that the range goes from 1 higher than the degree of the smaller polynomial to the degree of larger polynomial
        cosmall.append(0)
    for i in range(lengthind):
        polydifference.append(coefficients2[i]-coefficients1[i]) #Can do this because the changes made to cosmall and exposmall are simultaneously made to whichever polynomial is smaller
    while (polydifference[len(polydifference)-1] == 0) and (len(polydifference)-1 != 0): #This while loop cleans up the polynomial so that if the coefficient of the highest exponent is 0, it will be removed from the list
        polydifference.pop(len(polydifference)-1)
    return polydifference

def multiplymonopolys(monocoefficient,monoexponent,multicoefficients):
    #NOTE 1: The exponents should go from lowest to highest in order for this function to work
    #NOTE 2: Instead of expressing it as a list like most other polynomials, the single-term polynomial will have its exponent and corresponding coefficient expressed as an integer and float respectively
    coproduct = [] #This list stores the products of the coefficients of multicoefficients and monocoefficient
    exposum = []  #This list stores the sums of each exponent of multicoefficients and monoexponent
    for exponents in range(len(multicoefficients)):
        coproduct.append(multicoefficients[exponents]*monocoefficient)
        exposum.append(exponents+monoexponent)
        #When this happens, the order of exponents for exposum won't be from 0 to n, but from 0+monoexponent to n+monoexponent
    tempexpo = reverselist(exposum) #Because we want exposum to go from 0 to n+monoexponent while maintaining corresponging coefficients with coproduct, a reversed lists of both coproduct and exposum are created; note that tempexpo goes from n+monoexponent to 0+monoexponent
    tempco = reverselist(coproduct)
    length = len(tempexpo) #For the sake of the for loop below, the length of tempexpo is saved before any changes are made to the list
    for i in range(tempexpo[length-1]-1,-1,-1): #i will go from 0+monoexponent-1 to 0
        tempco.append(0)
    polyproduct = reverselist(tempco)
    while (polyproduct[len(polyproduct)-1] == 0) and (len(polyproduct)-1 != 0): #This while loop cleans up the polynomial so that if the coefficient of the highest exponent is 0, it will be removed from the list
        polyproduct.pop(len(polyproduct)-1)
    return polyproduct

print("Take note that these are the lists of coefficients in the polynomial going from LOWEST corresponding exponent to HIGHEST. For example, list [-1,0,1] would actually be (x^2)-1.")
print()
fpoly = [0,0,-28,0,0,1] #The definition for these polynomials are that they are the list of coefficients going from LOWEST corresponding exponent to HIGHEST
gpoly = [0,0,0,17]
print("f(x):",fpoly)
print("g(x):",gpoly)

rpoly = fpoly #The polynomial r(x) will start off as f(x)
qpoly = [0] #The polynomial q(x) will start off as 0x^0
while (rpoly != [0]) and (len(gpoly)-1 <= len(rpoly)-1): #The "(len(gpoly)-1 <= len(rpoly)-1)" part of the while loop establishes that as long as the degree of g(x) is less than or equal to that of r(x), the while loop can proceed
    LC = (rpoly[len(rpoly)-1])/(gpoly[len(gpoly)-1]) #LC represents the quotient of the leading coefficients of r and g
    LE = (len(rpoly)-1)-(len(gpoly)-1) #LE represents the difference between the leading exponents of r and g
    LTpoly = [LC] #LTpoly represents the polynomial created from the quotient of leading terms
    for k in range(LE-1,-1,-1): #k will go from one below the LE to 0, and 0 will be added to LTpoly for each iteration
        LTpoly.append(0)
    qpoly = addpolys(qpoly,reverselist(LTpoly)) #Using the reverse list function, a polynomial is created from the quotient of the leading terms going from lowest exponent to highest (LE in this case)
    gLT = multiplymonopolys(LC,LE,gpoly) #In order to determine a new r, the product of the monopolynomial LT and g(x) will be needed
    rpoly = subtractpolys(gLT,rpoly)
 
print("q(x):",qpoly)
print("r(x):",rpoly)