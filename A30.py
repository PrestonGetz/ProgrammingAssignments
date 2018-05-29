import random

print('Welcome to Hangman!')   
lines=open('wordbank.txt').read().splitlines()
myline=random.choice(lines)
word=myline
print(word)
guess=list('_'*len(word))

# Now ask the user to guess the word
while list(word)!=guess:
  print(' '.join(guess))
  #Step 3
  a=input("What letter do you guess?").upper()
  if a not in word:
    print('incorrect')
  else:
    i = 0
    while i<len(word):
      if list(word)[i]==a:
        guess[i]=a
      i+=1
print('You\'re right! it\'s ' + str(word) + '.')
