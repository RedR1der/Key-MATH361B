a0=int(input("What is the inital term in your sequence? "))
N=int(input("How many terms do you want in your sequence? "))
sequence=[a0]
lengthlist=[]
n=0
counter=0
flagVar=0

while len(sequence) != N:
    if sequence[n] % 2 == 0:
        sequence.append(sequence[n]/2)
    elif sequence[n] % 2 != 0:
        sequence.append(3*sequence[n]+1)
    n+=1

for number in sequence:
    if number != 1:
        lengthlist.append(number)
        counter+=1
    elif number==1:
        flagVar=1
        break

if flagVar != 0:
    #PROGRAMMER'S NOTE: "step" referes NOT to the number of terms in the sequence up to 1, but rather the number of times it took to get from one number to another.
    print("It took %d steps to get to 1." % counter)
else:
    print("Your sequence probably needs more terms to get to 1.")
    
print("Here is the list for the collatz conjecture:")
lengthlist.append(1)
print(lengthlist)