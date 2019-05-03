import random as r

def CheckForDistinct(mylist):
    for elements in mylist:
        if mylist.count(elements) != 1:
            return "This list has repeating values."
            break
    return "This list has distinct values."

N=int(input("To what factor of 2 do you want the size of the bit circle to be? "))
CircleSize=2**N
CircleIndicator=[] #This list will indicate the first N elements of the circle
for zeros in range(N):
    CircleIndicator.append("0")

Circles=[] #This list will show all possible circles with BitIndicator at the beginning
UniqueCircles=[] #This list will show all possible circles in Circles that have distinct N lengths bits
#Bits=[] #This list 

while len(Circles) != 2**(CircleSize-N):
    CircleArray=list(CircleIndicator)
    for i in range(N,CircleSize+(N-1)): #Because the circles we're looking at all have "0"s for the first N terms, we want to change the elements for all terms after that; note that the (N-1) will represent the number of elements that are at the beginning of CircleArray and are in an overlapped cycle
        CircleArray.append(str(r.randint(0,1)))
    for ii in range(N-1): #This for loop will equate the last N-1 terms with the first to represent an overlapping circle
        CircleArray[CircleSize+ii]=CircleArray[ii]
    if CircleArray not in Circles:
        Circles.append(CircleArray)

for j in range(len(Circles)): #This for loop looks at all N-length bits in a circle and determines if they are all distinct
    templist1=Circles[j]
    BitArray=[] #This list will store all N-length bits in a circle
    for jj in range(CircleSize):
        bit=""
        for bitparts in range(jj,jj+N):
            bit+=templist1[bitparts]
        BitArray.append(bit)
    if (CheckForDistinct(BitArray) == "This list has distinct values."):
        UniqueCircles.append(Circles[j])
        
UniqueSum=0 #This variable stores the sum of all concatenation of circles in UniqueCircles encoded as numbers
for k in range(len(UniqueCircles)):
    CircleString=""
    templist2=UniqueCircles[k] #This list store a circle with distinct N-length bits
    for kk in range(CircleSize): #This for loop stores the elements in templist2 in one continuous string
        CircleString+=templist2[kk]
#    print("Circle",k+1,":",CircleString) #NOTE: This line is optional; all it does is print out each circle
    UniqueSum+=int(CircleString,2)
print("The sum of the unique numeric representations for all binary circles of length 2 raised to %d is %d." %(N,UniqueSum)) 