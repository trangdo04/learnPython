import math

# sorting 
x = [4, 1, -6, 8]
x = sorted(x)
print(x)

# List Comprehensions
old_numbers = [x for x in range(20) if x % 2 != 0]
even_numbers = [2 * x for x in range(10)]
print(old_numbers)
print(even_numbers)

old_dict = {x : 2 * x + 1 for x in old_numbers}
print(old_dict)

set1 = {x * x for x in [2, -2, 3]}
print(set1)

zeroes = [0 for _ in even_numbers] 
print(zeroes)

pairs = {(x,y) for x in range(10) for y in range(x+1, 10)}
print(pairs)

# Functional tool
def checkPrime(n):
    r = 1
    for i in range(int(math.sqrt(n))):
        if n % (i+2) == 0 :
            r = 0
            break
    
    return r

n = 38
print(checkPrime(n))

# enumerate
fruits = ["applpes", "banana", "orange"]
name = "Trang"

for i in enumerate(fruits):
    print(i)

for count, i in enumerate(fruits):
    print(count)
    print(i)

for count, i in enumerate(fruits, 30):
    print(count)
    print(i)

for i, _ in enumerate(fruits):
    print("fruits: ", i)

# zip and Argument Unpacking
def sumOfList(*list):
    return sum(list)

list1 = ["an", "binh", "cong"]
list2 = [3, 5, 7]
s1, s2, s3 = zip(list1, list2)
print(s1)
print(s2)
ten, so = zip(s1, s2, s3)
print("ten: ", ten)
print("so: ", so)
print(sumOfList(*list2))
