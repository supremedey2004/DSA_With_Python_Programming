from os import remove

s = {1, 2, 3}
print(s)
s.add(4)
s.remove(2)
print(s)
#his will give error
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Union
print(A & B)  # Intersection


set2=set()
print(set2)
set4=set((2,8,8,4,5))
print(set4)

setx=set()
print(setx)
setx.add(3)
setx.add(4)
setx.add(5)
setx.add(6)
print(setx)



sety=set((2,8,58,7,1,6,2))
print(sety)
sety.remove()
print(sety)