import numpy as np
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
#This is the upper bound of the sum. It begins at 2 because ii needs to begin at 1
for i in range(N):    
    for ii in range(1,n):
        #The for loop runs through ii=1 up to n, storing the results of the equations into their respective temp lists
        element1=(np.log((ii**4)+ii+3))/((ii**0.5)+3)
        temp1=np.append(temp1,element1)
        element2=(np.exp(ii/100))/(ii**10)
        temp2=np.append(temp2,element2)
        element3=(np.sin((ii**2)+3*ii+6))*(18**-ii)
        temp3=np.append(temp3,element3)
    series_1[i]=sum(temp1)
    series_2[i]=sum(temp2)
    series_3[i]=sum(temp3)
    #The sum of the temp lists are stored into the series
    n+=1
    #For each element in the series Sn, we want the sum of the sequence up to n point, so the upper bound is increased
    temp3=np.array([])
    temp2=np.array([])
    temp1=np.array([])
    #The temp lists are cleared so that they may store the next elements in a sequence up to n
print("The first 15 elements in series 1 are", series_1[0:15],".\nThe last 15 elements are",series_1[-15:N],".")
print()
print("The first 15 elements in series 2 are", series_2[0:15],".\nThe last 15 elements are",series_2[-15:N],".")
print()
print("The first 15 elements in series 3 are", series_3[0:15],".\nThe last 15 elements are",series_3[-15:N],".")
