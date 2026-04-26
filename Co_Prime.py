a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=(max(a,b))
count=0
for i in range(1,c+1):
    if(a%i==0 and b%i==0):
        count=count+1
if count==1:
    print("These two numbers are co prime")
else:
    print("These two numbers are not co prime")