import time
import random

n = 1000
values = []
loops = 0
li = 0
sorting_done = False

def setup():
    global values
    global n

    for i in range(0, n):
        value = random.randint(0, n)
        values.append(value)
    

def sort():
    global values
    global loops
    global sorting_done
    global li

    # print(loops)
    lj = li + 1
    if loops < len(values):
        if values[li] > values[lj]:
            temp = values[lj]
            values[lj] = values[li]
            values[li] = temp
        
        li += 1
        
        if li > len(values) - 2 - loops:
            li = 0
            loops += 1 
    else:
        sorting_done = True
    
setup()
start = time.time()

while True:
    if not sorting_done:
        sort()
    else:
        break

end = time.time()
print(f"time took to sort {n} elements by bubble sort: {end - start}")
