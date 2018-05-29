import random
import sys

i = 0

def none():
  print(  ' _________')
  print(' |         |')
  print(' |')
  print(' |')
  print(' |')
  print(' |')
  print(' |')
  print(' |')
  print('========')
  
def one():
  print(  ' _________')
  print(' |         |')
  print(' |         O')
  print(' |')
  print(' |')
  print(' |')
  print(' |')
  print(' |')
  print('========')
  
def two():
  print(  ' _________')
  print(' |         |')
  print(' |         O')
  print(' |         |')
  print(' |')
  print(' |')
  print(' |')
  print(' |')
  print('========')
  
def three():
  print(  ' _________')
  print(' |         |')
  print(' |         O')
  print(' |         |-')
  print(' |')
  print(' |')
  print(' |')
  print(' |')
  print('========')
  
def four():
  print(  ' _________')
  print(' |         |')
  print(' |         O')
  print(' |        -|-')
  print(' |')
  print(' |')
  print(' |')
  print(' |')
  print('========')
  
def five():
  print(  ' _________')
  print(' |         |')
  print(' |         O')
  print(' |        -|-')
  print(' |          \ ')
  print(' |')
  print(' |')
  print(' |')
  print('========')
  
def six():
  print(  ' _________')
  print(' |         |')
  print(' |         O')
  print(' |        -|-')
  print(' |        / \ ')
  print(' |')
  print(' |')
  print(' |')
  print('========')

print('Welcome to Hangman!')   
lines=open('wordbank.py').read().splitlines()
myline=random.choice(lines)
word=list(myline)
c=0
guess=list('_'*len(word))

while list(word)!=guess:
  print(' '.join(guess))
  a=input("What letter do you guess?").upper()
  if a not in word:
    if c==0:
       none()
    if c==1:
      one()
      print("incorrect")
    if c==2:
      two()
      print("incorrect")
    if c==3:
        three()
        print("incorrect")
    if c==4:
      four()
      print("incorrect")
    if c==5:
      five()
      print("incorrect")
    if c==6:
      six()
      print("You lost! The correct answer is ",str(word),'.')
      sys.exit()
    c+=1
  else:
      i = 0
      while i<len(word):
        if list(word)[i]==a:
          guess[i]=a
        i+=1
print('You\'re right! it\'s ' + str(word) + '.')
sys.exit()
