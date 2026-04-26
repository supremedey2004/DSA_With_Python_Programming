str=input("Enter a string: ")
words=str.split(" ")
for x in words:
    if(x==x[::-1]):
        print("palindrom: ")
        print(x)
