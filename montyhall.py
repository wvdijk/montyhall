#!/usr/bin/env python3
from random import *

# construct door object
class Door:
  def __init__(self, name, isOpen, isPrize, isPick):
    self.name = name
    self.isOpen = isOpen
    self.isPrize = isPrize
    self.isPick = isPick
  def showProps(self): # (for debugging)
    print ("This is door %s, where isOpen is %s, isPrize is %s and isPick is %s" % (self.name, self.isOpen, self.isPrize, self.isPick))

# filter function to find doors you can open
def getopendoors (obj):
    return bool(obj.isPick == False and obj.isPrize == False)


winswitch = 0
winstay = 0
times = 100 # no. of times to do this
rnd = 0

# here we go
for i in range(times):
    rnd +=1;
    #create doors, put them in an array
    door1 = Door("1", False, False, False)
    door2 = Door("2", False, False, False)
    door3 = Door("3", False, False, False)
    doors = [door1, door2, door3]

    #randomly assign prize and pick
    pick = randint(0,2)
    prize = randint(0,2)
    doors[pick].isPick = True
    doors[prize].isPrize = True

    print("=== Round %d ===" % rnd)
    print("You picked door %s" % doors[pick].name)
    print("The prize is behind door %s" % doors[prize].name)

    #now find a door to open - we don't really need to do this, but hey, for science
    doorstoopen = list(filter(getopendoors, doors))
    if len(doorstoopen) > 1: # two doors in list (i.e., picked winner)
        x = randint(0,1) # randomly open one
        doorstoopen[x].isOpen = True
        print("I'm opening door no. %s" % doorstoopen[x].name)
    else: # just one door in list, since player picked a losing door
        doorstoopen[0].isOpen = True
        print("I'm opening door no. %s" % doorstoopen[0].name)

    if doors[pick] == doors[prize]:
        print("If you switched, you lose")
        winstay+=1
    else:
        print("If you switched, you win")
        winswitch+=1

print("Played %d times. Switching would yield %d wins and %d losses." % (times, winswitch, winstay))
