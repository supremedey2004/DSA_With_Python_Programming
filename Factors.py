a=int(input("Enter a Number: "))
print("The factors are")
for i in range(1,a+1):
    if(a%i==0):
        print(i)