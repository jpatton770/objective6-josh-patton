#discount counter
#imports
import random
#subr to print off %
def discounter(disc):
  while disc < 50: #parameter for the loop
    disc = disc + random.randint(1,15) #adds random amount every time
    print("the sale is at {} % off".format(disc)) #prints off values
  print("the sale is at 60 % off") #prints final value
#mainpg
discounter(10) #runs subr



