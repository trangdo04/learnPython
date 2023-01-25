"""a = input("nhap so nguyen a: ")
b = input("nhap so nguyen b: ")
c = input("nhap so nguyen c: ")
print(float(a + b + c))

x = input()
y = input()
print(x + y)"""

length = int(input())
numbers = []

for i in range(0, length):
    numbers.append(int(input()))

for i in range(0, length):
    for j in range(i+1, length):
        if (numbers[i] > numbers[j]):
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp

print(numbers)