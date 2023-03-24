li=[15,47,50.34,"Auro",15,60]
print(li)

#count(no. of times that value present)
print(li.count(15))

#Index
print(li.index(50.34))

#insert
li.insert(80,83)
print(li)

#pop (remove 5th value)
li.pop(5)
print(li)

#extend
li2=["Anaya",500,False]
li.extend(li2)
print(li)

#copy
li3=li.copy
print(li)

#sort
li4=[15,74,8,36,25,84,67]
li4.sort()
print(li4)

#reverse
li4.reverse()
print(li4)

#nestedList
li5=[15,74,"Aman",[40,78,"Akash",[60,85]]]
print(li5)

#ListUnpacking
li6=["Ankush","Sitara"]
n1,n2=li6
print(n1)
print(n2)


o/p
[15, 47, 50.34, 'Auro', 15, 60]
2
2
[15, 47, 50.34, 'Auro', 15, 60, 83]
[15, 47, 50.34, 'Auro', 15, 83]
[15, 47, 50.34, 'Auro', 15, 83, 'Anaya', 500, False]
[15, 47, 50.34, 'Auro', 15, 83, 'Anaya', 500, False]
[8, 15, 25, 36, 67, 74, 84]
[84, 74, 67, 36, 25, 15, 8]
[15, 74, 'Aman', [40, 78, 'Akash', [60, 85]]]
Ankush
Sitara
