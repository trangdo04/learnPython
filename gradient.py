import math

def f(x):
    return 4 * pow(x, 2) + 3 * x + 1

def gradientX(x):
    return 8 * x + 3

if __name__ == "__main__":
    k = 0.01
    e = 0.000001
    x = int(input())
    prev = f(x)
    nextX = f(x) + e + 1
    
    while abs(prev - nextX) > e :
        prev = f(x)
        x = x - k * gradientX(x)
        nextX = f(x)
    
    print("x la: ", x, "--- f(X) la: ", f(x))