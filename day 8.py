#1. Merge 2 dictionaries :

d1 = {"apple" : 3,"orange":4,"litchi" : 7}
d2 = {"grapes" : 5,"banana" : 12}
print("dictionary 1: ",d1,"\ndictionary 2: ",d2)
d1.update(d2)
print("\nMerged Dictionary",d1)

#2. Sorting a list and converting it to a set

lst = ["A for apple","Z for zebra","Q for quil","G for God loves me"]
print("List : ",lst)
Ascending = sorted(lst)
print("Ascending : ",Ascending)
Descending = sorted(lst,reverse=True)
print("Descending : ",Descending)
print("Set : ",set(lst))

#3. Length of dictionary and sorting dictionary
print(len(d1))
dictionary = dict(sorted(d1.items()))
print(dictionary)

#4. CHANGE CHAR IN A STRING
s1 = input("String ")
n = int(input("Index to change"))
s_list = list(s1)
s_list[n] = 'B'
s2 = "".join(s_list)
print(s2)

#5.Capitalise first letter of string
s3 = input("Big string please : ")
print(s3.title())
#6. Repeated items of a list
l1 =[1,2,3,4,3,4,5,1,2,3,7]
empty = {}
duplicates = []
for item in l1:
    if item not in empty:
        empty[item]=1
    else:
        empty[item]+=1
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)

#7.sum and divide
a,b,c = [int(x) for x in input("Enter 3 numbers: ").split()]
d = int(input("Enter the divisor : "))
sum_ = (a+b+c)/d
print(sum_," is the answer")

#8. mean median and mode of 3 numbers
import numpy as np

arr = [1,2,3,4,5,6,7,8,1,2,3,1,2,1,1,1,5,5,5,5,5,3,3]
print("mean ",np.mean(arr))

print("median ",np.median(arr))
#9.swap cases
string = "SaVaGe LoVe"
print(string.swapcase())

#10.integer to binary and octal
n = int(input())
dig = 0
i=1
print("Decimal to binary with function",bin(n))
print("Decimal to Octal with function",oct(n))
while n>0:
    rem = n%2
    dig= dig+rem*i
    n=n//2
    i*=10
print("Binary without function ",dig)

