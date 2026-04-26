count=0
name="Banana"
for i in range(0,len(name)):
    if name[i] in "AEIOUaeiou":
        count=count+1
print("Total Vowel count is",count)
print()
count=0
for ch in name:
    if ch.lower() in ['a','e','i','o','u']:
        count=count+1
print("Total Vowel count is",count)