#tuple is a collection of elements which are ordered and is immutable

mytuple=(1,5,"hello",9.4,5,33)

print(mytuple)
print(mytuple[0])
print(mytuple[-2])
print(len(mytuple))

x=mytuple.count(5)
print(x,"times")

y=mytuple.index("hello")
print(y,"position")

newtuple=(5,2,7,4.29,"hii","ok")

jointuple=mytuple+newtuple

print(jointuple)
