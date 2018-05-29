import random
num = random.randint(0,100)
guess = int(input("Guess a number: "))
count = 0
while count == 0:
  if guess == num:
    print("This is the right number!")
  elif guess > num:
    print("This number is too high.")
  elif guess < num:
    print("This number is too low.")
