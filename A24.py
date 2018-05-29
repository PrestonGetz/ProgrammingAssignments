# imports. If you need to import anything, please place here.
import time
# inputs
name=input('Enter your name: ')
num_of_stars = int(input('Please Enter the rows of stars you would like to print: '))
count = int(input('What number do you want to count to? '))
array = input('Please enter an array of numbers separated by spaces to check for duplicates.\n').split()
array = [int(x) for x in array]
# Exercise 1 function
def backwardsname():
  backwards=[]
  namearray=list(name)
  for x in name:
    backwards.append(namearray[-1])
    namearray.remove(namearray[-1])
  backname=''.join(backwards)
  print(backname)
# Exercise 2 function
def starsinrows():
  star="*"
  for x in range(num_of_stars):
    print(star)
    star +='*'
# Exercise 3 function
def timer():
  timecount=0
  for x in range(count):
    timecount+=1
    print(str(timecount))
    time.sleep(1)
# Exercise 4 function
def checkduplicates():
  x = []
  for value in (array):
    if value not in x:
      x.append(value)
  return x
  print(checkduplicates())

# Call all your functions here.
backwardsname()
starsinrows()
timer()
checkduplicates()
