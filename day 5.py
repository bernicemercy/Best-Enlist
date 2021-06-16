    #---------LIST OPERATIONS--------- 
print("\tLIST OPERATIONS\n")
lst = list([x for x in input("ENTER ELEMENTS OF LIST : ").split()])

#append an item to a list
print("LIST : ",lst)
print("Element to Append : ")
lst.append(input())
print(lst)

#add element at a specific index
print("Adding element at an index")
lst.insert(int(input("index: ")), input("element : "))
print(lst)


#to delete an element at index
del lst[int(input("index to delete : "))] #del element in the list
print(lst)

#pop element from the list
print("Pop operation")
lst.pop()
print(lst)

lst.pop(int(input("index to pop : ")))
print(lst)

#remove an element from list
lst.remove(input("Element to be removed : "))
print(lst)

#maximum and minimum in a lst
print("Maximum value : ",max(lst))
print("Minimum value : ",min(lst)) 

    #--------TUPLE OPERATIONS--------------
tup = tuple(x for x in input("\n\t TUPLE OPERATIONS \n ENTER ELEMENTS OF TUPLE : ").split())
print(tup)

print("Reverse of the tuple")
print(tup[::-1])
print("Tuple converted to list",list(tup))
