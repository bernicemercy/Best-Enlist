# 1. creating functions to perform arithmetic operations

def add(a,b):
    c =a+b
    print("Addition ",c)
def sub(a,b):
    c =a-b
    print("Subbtraction ",c)
def mul(a,b):
    c =a*b
    print("Multiplication ",c)
def div(a,b):
    c =a/b
    print("Division ",c)



a,b = [int(x) for x in input().split()]
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)

#2.Covid patient Details

def covid(name,temp):
    print("Name : ",name," Temperature : ",temp)

name = input()
temp = 98
covid(name,temp)
    
