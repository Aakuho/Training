import time
import random

def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        
        fname = func.__name__
        print(f"{fname} took {round(after-before, 3)} seconds to execute")
        return value
    return wrapper

@timed
def bubbleSort(arr): # Got the code from Geeksforgeeks.com
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            #return
            ...
    ...

@timed
def own(arr): # Thought of this randomly, and it actually works
    l = [None for i in range(max(arr))]
    return_value = []

    for value in arr:
        if not type(l[value - 1]) == int:
            l[value - 1] = 1
        else:
            l[value - 1] += 1
    
    for index, value in enumerate(l):
        if value:
            if value <= 1:
                return_value.append(index + 1)
            else:
                for i in range(value):
                    return_value.append(index + 1)
    
    #return return_value # I dont want to print 10 000+ values
    ...
        


def create_array(len):
    l = [random.randint(1, 100) for i in range(len)]
    return l

print(own(arr=create_array(10000))) # >>> own took 0.003 to execute
print(bubbleSort(arr=create_array(10000))) # >>> bubbleSort took 6.449 seconds to execute