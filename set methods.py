#add() method

theset={"apple","banana","cherry"}
theset.add("orange")
print(thisset)

#update() method

theset={"doremon","nobita","sizchuka"}
theset.update(["pogo","cartoon","chotta bheem"])
print(theset)

#len() method

theset={"apple","banana","cherry"}
length=len(theset)
print(length)

#remove method

theset={"apple","orange","banana"}
theset.remove("banana")
print(theset)

#discard() method

theset={"apple","cherry","banana"}
theset.discard("apple")
print(theset)

#pop() method

theset={"apple","cherry","blossom"}
x=theset.pop()
print(x)
print(theset)

#clear() method 
theset={"apple","orange","banana"}
theset.clear()
print(theset)

#delete() method

theset={"apple","orange","banana"}
del theset
print(theset)

#union()

set1={"a","b","c"}
set2={"1","2","3"}
set3=set1.union(set2)
print(set3)

#update()

set1={"a","b","c"}
set2={"1","2","3"}
set1.update(set2)
print(set1)

#copy()

names={"steve","nick","rick"}
names2=names.copy()
names2.add("glenn")
print(names2)
