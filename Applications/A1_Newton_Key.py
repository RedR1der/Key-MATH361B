import numpy as np
import math

N=100
TOL=1e-4
z0=float(input("Enter the first iteration: "))
#f_z = lambda z: ((1/100)*z**4)+((1/100)*(math.e-2-2**0.5)*z**3)+(1/100)*((2**1.5)-(math.e*2**0.5)-3-2*math.e)*(z**2)+(1/100)*((2**1.5)*math.e+(3*2**0.5)-3*math.e)*z+(3/100)*(2**0.5)*math.e
f_z = lambda z: math.tan(z)-z-2
#df_z = lambda z: (0.04*z**3)+(0.03*(math.e-2-2**0.5)*z**2)+(0.02*((2**1.5)-(math.e*2**0.5)-3-2*math.e)*z)+0.01*((2**1.5)*math.e+(3*2**0.5)-3*math.e)
df_z = lambda z: (math.cos(z)**-2)-1
NewtonsArray=np.zeros((N))
NewtonsArray[0]=z0
SpacingArray=np.zeros((N-1))
breakindicator=0

for i in range(1,N):
    NewtonsArray[i]=(NewtonsArray[i-1])-((f_z(NewtonsArray[i-1]))/(df_z(NewtonsArray[i-1])))
    SpacingArray[i-1]=NewtonsArray[i]-NewtonsArray[i-1]
    if np.abs(NewtonsArray[i]-NewtonsArray[i-1]) < TOL:
        breakindicator=NewtonsArray[i]
        break

print("Here are the iterations of z:")
print(NewtonsArray)
print("Here are the spaces between each iteration of z:")
print(SpacingArray)
print("The sequence falls below the tolerance at",breakindicator)