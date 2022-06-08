# There are 100 holes (0 - 99) in a field and in one of them is a rabbit.
# You need to find the rabbit, you're only allowed to go through the holes one at a time.
# and everytime you go through a hole the rabbit jumps to the adjacent hole.
#
# For example:
# _ _ r _  if there are 4 holes and the rabbit is at hole 2
# 0 1 2 3  
#
# and we start from hole 0, the rabbit must jump to one of the adjacent holes: [1, 3], let's pick 3 
# _ _ _ r
# 0 1 2 3
# 
# next we check hole 1, the rabbit must jump to the adjacent hole that's only 2 in this case
# _ _ r _
# 0 1 2 3
#
# next we check hole 2, that's where the rabbit is, we've successfully found the rabbit.
#
#
# hint: if the rabbit initally is at even hole we should start searching from even hole, 
# if rabbit intially starts at odd hole we should start searching from odd hole.
# otherwise rabbit can jump over us and we will never find the rabbit.
# 

import math
import random
from re import L


noOfHoles = 100
rabbitPos = random.randint(0, noOfHoles - 1)
# rabbitPos = 11

def moveRabbit():
    global rabbitPos
    currentPos = rabbitPos

    if (rabbitPos == noOfHoles - 1):
        return rabbitPos - 1

    move = random.randint(0, 1)

    if move == 0:
        rabbitPos -= 1
    else:
        rabbitPos += 1

    print("Moving the rabbit from {} to {}".format(currentPos, rabbitPos))
    return rabbitPos

def lookForRabbit(holes, rabbitPos):
    if rabbitPos == holes:
        return True
    else:
        return False


found = False
for i in range(0, noOfHoles):
    print("Looking for the rabbit in hole {}".format(i))
    if (i == rabbitPos):
        print("Found the Rabbit.")
        found = True
        break
    
    rabbitPos = moveRabbit()

if not found:
    for i in range(1, noOfHoles):
        print("Looking for the rabbit in hole {}".format(i))
        if (i == rabbitPos):
            print("Found the Rabbit.")
            found = True
            break
    
        rabbitPos = moveRabbit()

if not found:
    print("Not found.")