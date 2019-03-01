import numpy as np

PyTrip=int(input("Enter a sum of a pythagorean triple: "))
Pymat=np.zeros([0,3])
Tripmat=np.zeros([0,4])

for bb in range(2,PyTrip):
    b=float(bb)
    for aa in range(1,bb):
        a=float(aa)
        c=((b**2)+(a**2))**0.5
        if c.is_integer()==True:
            Tripmat=np.vstack([Tripmat,np.array([a,b,c,a+b+c])])
            if a+b+c==PyTrip:
                print("For a sum of %d:" % (PyTrip))
                print("Leg 1:",a)
                print("Leg 2:",b)
                print("Hypotonuse:", c)
                print()

print()
print("The following is a matrix of right triangles that have natural numbers for all sides and the sum of their sides:")
print(Tripmat)