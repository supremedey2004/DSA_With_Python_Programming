name="AnEErtUU"
count=0
for i in range(0,len(name)):
    if name[i] in "aeiouAEIOU":
        count=count+1
print(count)