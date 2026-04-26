num=153
fixed=num
total=0
while num>0:
    digit=num%10
    num=num//10
    total=total+digit**3
if total==fixed:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")