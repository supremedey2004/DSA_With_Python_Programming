a=int(input("Enter a Number: "))
b=int(input("Enter another Number: "))
c=min(a,b)
d=[]
for i in range(1,c+1):
    if(a%i==0 and b%i==0):
        d.append(i)
print(max(d))