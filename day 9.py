lst =[1,2,3,4,5,6,7]
print("Original list : ",lst)
for i in range(len(lst)):
    lst[i] += 2
print("After adding 2 : ",lst)

#2. pattern
n = int(input("Pattern : "))
for i in range(0,n):
    for j in range(n-i,0,-1):
        print(j,end = ' ')
    print("\n")

#3. fibonnocci series
num = int(input("Fibonnocci Series : "))
a = 0
b = 1
s = 0
c = 0
while(c<n):
    print(s,end=' ')
    c+=1
    a = b
    b = s
    s = a+b
    
#4.Armstrong number

arm = int(input("\nArmstrong number or not : "))
s2 = 0
t = arm
while(arm>0):
    rem = arm%10
    s2 += rem**3
    arm//=10
if(t == s2):
    print("armstrong")
else:
    print("not armstrong")

#5.9 tables

for i in range(1,11):
    print("9 X ",i," = ", 9*i)

#6. negative or positive

x = int(input("Negative or positive : "))
if x>0 :
    print("Positive")
elif x<0 :
    print("Negative")
else:
    print("Zero")

#7. days to ages

days = int(input("Days : "))
print("Age : ", days//365)

#8. Trignometric function

import math
trig = input("Trignometric function : ")
deg = int(input("Degree"))
if trig=='sin':
    print(math.sin(deg))
elif trig=='cos':
    print(math.cos(deg))
elif trig=='tan':
    print(math.tan(deg))
elif trig=='cosec':
    print(math.cosec(deg))
elif trig=='sec':
    print(math.sec(deg))
else:
    print("does not exist")

#9. Calculator
y,z = [int(x) for x in input("Two numbers : ").split()]
o = input("Operator : ")
if o == '+':
    print(y+z)
elif o=='-':
    print(y-z)
elif o == '*':
    print(y*z)
elif o == '/':
    print(y/z)
elif o == '//':
    print(y//z)
elif o =='%':
    print(y%z)
elif o =='**':
    print(y**z)
else:
    print("DoEs NoT ExIsT")

    
