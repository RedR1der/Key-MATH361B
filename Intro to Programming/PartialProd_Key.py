import numpy as np
#Function for finding product in a list
def prod(myList):
    ident=1
    for k in myList:
        ident*=k
    return ident
#----------------------------------------------------------------------------------------------------------------------------
N=int(input("Enter an interger N: "))
series_1=np.zeros((N))
series_2=np.zeros((N))
series_3=np.zeros((N))
#Three lists consisting of all 0s are created at N length
temp3=np.array([])
temp2=np.array([])
temp1=np.array([])
#These three lists will be used to store the elements of the equation as the go up to n
n=2
n1=3
#This is the upper bound of the partial product. It begins at 2 because ii needs to begin at 1. Note that there's n1, which equals 3 because series 1 starts at iii=2
for i in range(N):    
    for ii in range(1,n):
        #The for loop runs through ii=1 up to n, storing the results of the equations into their respective temp lists
        element2=(np.exp(ii/100))/(ii**10)
        temp2=np.append(temp2,element2)
        element3=(1/ii)
        temp3=np.append(temp3,element3)
    for iii in range(2,n1):
        element1=((iii**3)-1)/((iii**3)+1)
        temp1=np.append(temp1,element1)
    series_1[i]=prod(temp1)
    series_2[i]=prod(temp2)
    series_3[i]=prod(temp3)
    #The product of the temp lists are stored into the series
    n+=1
    n1+=1
    #For each element in the series Sn, we want the product of the sequence up to n point, so the upper bound is increased
    temp3=np.array([])
    temp2=np.array([])
    temp1=np.array([])
    #The temp lists are cleared so that they may store the next elements in a sequence up to n
print("The first 15 elements in series 1 is", series_1[0:15],".\nThe last 15 elements are",series_1[-15:N],".")
print()
print("The first 15 elements in series 2 is", series_2[0:15],".\nThe last 15 elements are",series_2[-15:N],".")
print()
print("The first 15 elements in series 3 is", series_3[0:15],".\nThe last 15 elements are",series_3[-15:N],".")
