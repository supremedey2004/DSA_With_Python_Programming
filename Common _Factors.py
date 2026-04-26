a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=(min(a,b))
for i in range(1,c+1):
    if(a%i==0 and b%i==0):
        print(i)