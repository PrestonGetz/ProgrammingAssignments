def a1():
  firstnum=int(input("First number:"))
  secondnum=int(input("Second number:"))
  thirdnum=int(input("Third number:"))
  print("The sum is: ",firstnum+secondnum+thirdnum)
def a2():
  base=int(input("What is the base of the triangle?"))
  height=int(input("What is the height of the triangle?"))
  print("The area of the triangle is: ",base*height/2)
def a3():
  name=(input("What is your name?"))
  print("Hello, "+name)
def a4():
  num1=int(input("First number:"))
  num2=int(input("Second number:"))
  if num1>num2: 
    print("The bigger number is ",num1)
  if num2>num1:
    print("The bigger number is ",num2)
def a5():
  food_items = ["turkey","ham", "spam","eggs","nuts"]
  print(food_items[3])
  for x in food_items:
    print(x)
def a6():
  grade=int(input("Enter your grade: "))
  if grade < 60:
    print('F')
  elif grade < 70:
    print('D')
  elif grade < 80:
    print('C')
  elif grade < 90:
    print('B')
  elif grade >= 90:
    print('A')
def a7():  
  array=[1, 1, 2, 3, 4, 5, 8, 11, 13, 17, 19, 20, 21, 34, 43, 55, 89]
  array2=[]
  for x in array:
    if x <30:
      array2.append(x)
  print(array2)
a1()
a2()
a3()
a4()
a5()
a6()
a7()
