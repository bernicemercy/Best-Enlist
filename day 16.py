#1
z = lambda x,y:x*y
x,y = [int(x) for x in input().split()]
print(z(x,y))
#2
def fibonacci(count):
    sequence = [0, 1]

    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count)))

    return sequence[:count]

print(fibonacci(10))

#3
lst = [1,2,3,4]
for i in range(len(lst)):
    lst[i] *= 5
print(lst)

#4
nums = [3,6,9,12,15,18,27,22,90]
result = list(filter((lambda x: x%9==0),nums))
print(result)

#5
n = [1,2,3,4,5,6,7,8,9,10,11,12,13]
results = list(filter((lambda x:x%2==0),n))
print(len(results))
