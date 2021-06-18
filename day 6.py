#1).Merging Two Dictionaries

d1 = {'a': 1, 'b': 2}
print ("Dictionary 1 = " , d1)

d2 = {'c': 3, 'd': 4}
print ("Dictionary 2 = " , d2)

dicti = d1.copy()
dicti.update(d2)
print("Combined Dictionary = " , dicti)

#2).Removing a key from the Dictionary

M={'apple': 100, 'banana': 200, 'cherry': 300, 'pear': 400}
print("Dictionary = " , M)

if 'apple' in M: 
    del M['apple']
print("Dictionary after deletion " , M)

#3).Mapping two lists into a dictionary

keys = ['Sachin', 'Dhoni', 'Raina' , 'kholi' , 'Rahul']
print("List1 Player Names : " , keys)

values = ['10','7', '3' , '18' , '1' ]
print("List2 Player Numbers : " , values)

New_Dict = dict(zip(keys, values))
print("Indian Cricketers Jersey Numbers : " , New_Dict)

#4).Finding the length of a set

s = {"dog","cat" ,"fish", "parrot", "rat"}
print("Set = " ,s)

print("Length of the Set = " , len(s))


#5).Removing the intersection of a 2nd set from the 1st set
set1 = {103,205,307,409,507,602}
set2 = {1,0,5,7,8,9,2}
print("Original sets:")
print("Set 1 = " , set1)
print("Set 2 = " , set2)

set1-=set2
print("\nRemoving the intersection of a 2nd set from the 1st set")
print("Set 1 = " , set1)
print("Set 2 = " , set2)
