from creatgraph import *
import time

def selectSort(arr, n, sleep):
    generate(arr)
    if n >= len(arr) -1:
        print(arr)
        return
    min = arr[n]
    index = n
    test = True
    for numbers in range(n,len(arr)):
        if(min > arr[numbers]):
            min = arr[numbers]
            index = numbers 
            arr[index] = arr[n]
            arr[n] = min
            test = False
    if test == True:
        arr[index] = arr[n]
        arr[n] = min   


    swap = 0
    swap = arr[index]
    arr[n] = min
    arr[index] = swap
    
    n = n + 1
    print(arr)
    time.sleep(sleep)
    selectSort(arr, n, sleep)


selectSort([5,8,2,7,1,3,9,13,11], 0, 2)