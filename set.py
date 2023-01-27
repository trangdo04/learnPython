import types

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