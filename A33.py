import random;h,t,sides,flips,outcome=0,0,[0,1],int(input('How many times do you want to flip a coin?\n')),0
for x in range(flips):outcome+=random.choice(sides);t=flips-outcome
print("Total Coin Flips\n================\nHeads: ",str(outcome),"\nTails: ",str(t))
