list1 = [9,4,2,6,3,0]
list2 = [2,3,4,5,6,7]
tup = tuple(zip(list1,list2))
print(tup)

lst3 = ["Cs","ECE","EEE","IT","Mech","Agri","Pharm","Bio med"]
l = []
for i in range(0,8):
    l.append(i)
print(list(zip(lst3,l)))
lst = sorted(list1,reverse = False)
print(lst)

odd = filter(lambda x: x%2!=0,list1)
print(list(odd))
