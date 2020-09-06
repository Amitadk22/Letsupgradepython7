#set is a collection of elements whic are unordered and unindexed

myset={"apple",1,0.4}
print(myset)
#print(myset[0]) ----> error
print(len(myset))

myset.add("mango")
print(myset)

myset.update(["grapes",23,9])
print(myset)

myset.remove(0.4)
print(myset)

myset.discard(0.4)
print(myset)

x=myset.pop()
print(x)

cpyset=myset.copy()
print(cpyset)

myset.clear()
print(myset)

del myset
print(myset)  #error as myset doesnt exist
