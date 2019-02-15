import matplotlib.pyplot as plt
import numpy as np

def func_name(param1, param2):
    N=int(input("How many points do you want in your plot? "))
    xVals=np.linspace(param1,param2,N)
    myYs=[]
    for x in xVals:
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
    finPlot=plt.plot(xVals,myYs)
    return finPlot

startPt=float(input("What is your starting x value? "))
endPt=float(input("What is your ending x value? "))
aPlot=func_name(startPt,endPt)
titPlot=plt.title("I.7 Piecewise Function")
yLabel=plt.ylabel("y")
xLabel=plt.xlabel("x")
print(aPlot)