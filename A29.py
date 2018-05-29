import random
lines=open('wordbank.txt').read().splitlines()
myline=random.choice(lines)
word=list(myline)
print(word)
#I realized later that I only had to randomly generate a word, but im going to keep this in case I need it later >
ammount=len(word)
print('-'*ammount)
#.....^
