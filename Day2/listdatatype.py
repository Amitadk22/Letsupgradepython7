#list is a collection of data elements which is ordered and is muttable

lst=[1,5,"hii",0.5]
print(lst)
print(lst[1])
print(lst[-2])
print(lst[:2])
print(len(lst))

lst[2]="hello"
print(lst)

for x in lst:
    print(x)

#inserting into the list
lst.append(50)
print(lst)

lst.insert(0,"lup")
print(lst)



#copying a list to another

mylist=lst.copy()

#counting the number of times a particular element is repeated
y= lst.count("lup")
print(y)

#removing element from the specified index
lst.remove(50)
print(lst)

#removing all the elements from the list
lst.clear()
print(lst)
