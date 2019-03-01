import numpy as np

#(func name) = lambda (input): (equation using input)


#a_n = lambda n: 1+((2*n+1)/(5*n+3))


#a_n = lambda n: 1+((n**2)/(n**3))
a_n = lambda n: 1.0+(1)**n
#a_n = lambda n: n
N=int(input("Enter the number of terms in your series: "))
series=np.zeros((N))
startVar=1

for ii in range(N):
    startVar*=a_n(ii+1)
    series[ii]=startVar

print("The first 15 terms of the series are:")
for firstT in series[0:15]:
    print("-%f"%(firstT))
print()
print("The last 15 terms of the series are:")
for lastT in series[-15:N]:
    print("-%f"%(lastT))