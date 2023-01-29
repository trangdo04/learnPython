import types
import math
# setOfEvenNumbers = []

# n = int(input())

# for i in range(0, n):
#     if (i % 2 == 0):
#         setOfEvenNumbers.append(i)

# print(setOfEvenNumbers)

# function, Strings, Dictionary, Set, Lists
# Sap xep mot mang tang dan theo thu tu chan
# Học hết phần The Not-so-basic tu trang 27

# dictionary
mydict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print("len", len(mydict))
print(type(mydict))
print(mydict)

# function
def primeNumbers(n):
    for i in range(0, n):
        if (n % (i+2) == 0):
            return 0
        
        if (i > n/2):
            return 1

print(primeNumbers(11))\

#set
myset = {1, 2, 3, 4, 5, 6, 7, "trang"}
print(myset)
set1 = {3.4, 6, "do", 7}
myset.update(set1)
print(myset)
print(type(myset))

#list
mylist = [1, "trang", 2, 3, 4]
print(mylist)
print("type", type(mylist))
print("phan tu thu 3: ", mylist[2])
print("ptu cuoi: ", mylist[-1])
print("bo 3 phan tu dau: ", mylist[3:])
print("3 phan tu dau: ", mylist[:3])
print(mylist[-2:])
print(mylist[2:4])

# Sap xep mot mang tang dan theo thu tu chan
n = int(input())
mang = []

for i in range(0, n):
    mang.append(int(input()))

for i in range(0, math.floor((n-1)/2)):
    for j in range(i+1, math.floor((n-1)/2) + 1):
        if (mang[i * 2] > mang[j * 2]):
            tmp = mang[i * 2]
            mang[i * 2] = mang[j * 2]
            mang[j * 2] = tmp

print(mang)