#dictionary is a collection of elements with keys all their values

mydict={"fname":"Jai" ,"lname":"Prakash" ,"year":"1992" ,"work":"Software Engineer"}

print(mydict["fname"])
print(len(mydict))

mydict["company"]="Google"
print(mydict)

newdict=mydict.copy()

x=mydict.get("company")
print(x)

mydict.pop("year")
print(mydict)

mydict.popitem()
print(mydict)

mydict.clear()
print(mydict)
