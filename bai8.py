import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr, float)
    arr = arr[::-1]
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true&h_r=next-challenge&h_v=zen