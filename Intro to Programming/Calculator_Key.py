StoreList=[0,0,0,0,0]
x=float(input("Enter a number for x:"))
y=float(input("Enter a number for y:"))
z=float(input("Enter a number for z:"))

StoreList[0]=x+y
StoreList[1]=(y*z)+(3*x)
StoreList[2]=(StoreList[0])**2
if StoreList[0]!=0:
    StoreList[3]=(2*StoreList[1]-0.5*x)/StoreList[0]
else:
    StoreList[3]="Undefined"
StoreList[4]=7%3
print("The list before bulletin three is",StoreList) #Temporary

StoreList[2]+=3
StoreList[4]*=0.75
print("The list after bulletin three is",StoreList)
print("The sum of the list is",sum(StoreList))
