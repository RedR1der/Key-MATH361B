import matplotlib.pyplot as plt
import numpy as np

def func_name(param1):
    myYs=[]
    for x in param1:
        if x < -2:
            myYs.append(-3*((x+2)**2)+1) #V
        elif (x >= -2) and (x < -1):
            myYs.append(1) #V
        elif (x >= -1) and (x <= 1):
            myYs.append(((x-1)**3)+3) #V
        elif (x > 1) and (x < 2):
            myYs.append(np.sin((np.pi)*x)+3) #V
        else:
            myYs.append(3*np.sqrt(x-2)+4) #V
    finPlot=plt.plot(param1,myYs)
    return finPlot

N=int(input("How many points do you want in your plot? "))

xVals=np.linspace(-3,3,N)

aPlot=func_name(xVals)
titPlot=plt.title("I.7 Piecewise Function")
yLabel=plt.ylabel("y")
xLabel=plt.xlabel("x")

print(aPlot)