# Look at A22 to read from an array-56
import collections

def dice_rolling():
    rolls=int(input("Rolls: "))
    answer=[]
    for roll in range(rolls):
        roll=input("What are the rolled numbers?").split()
        value=sorted([x for x in collections.Counter(roll).values()])
        if sorted(roll)==['2','3','4','5','6']:
            answer.append('big-straight')
        elif sorted(roll)==['1','2','3','4','5']:
            answer.append('big-straight')
        elif value==[5]:
            answer.append('five-in-a-row')
        elif value==[1,4]:
            answer.append('four-of-a-kind')
        elif value==[2,3]:
            answer.append('three-of-a-kind')
        
        
        else:
            answer.append('no answer')
    print(''.join(answer))
dice_rolling()
'''
import random

rolls=[]

cases=int(input("how many cases?"))
for x in range(0,3):
    for x in range(0,5):
        rolls.append(random.randint(1,6))
print(rolls)
'''
