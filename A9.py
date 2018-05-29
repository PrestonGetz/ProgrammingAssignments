word = input("Please enter a word:")
drow = word[::-1]
if word == drow:
  print("This word is a palindrome!")
else:
  print("This word is not a palindrome!")
