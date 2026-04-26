num = 334
sum = 0
while (num > 0):
    digit = num%10
    sum=sum+digit
    num=num//10
print(sum)
num = int(input("Enter a number: "))
n = num
power = len(str(num))
total = 0
