print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    try:
        choice=int(input("Enter choice(1/2/3/4):"))
        if choice>=1 and choice<=4:
            break
        else:
            print("Your input was not a number between 1 and 4")
    except ValueError:
        print("Your input was not a number between 1 and 4")
def Add():
    answer=a+b
    print(str(answer))
def Subtract():
    answer=a-b
    print(str(answer))
def Multiply():
    answer=a*b
    print(str(answer))
def Divide():
    try:
        answer=a/b
        print(str(answer))
    except:
        print("Divide by zero")
while True:
    try:
        a=int(input("Enter first number:"))
        break
    except ValueError:
        print("Your input was not a number")

while True:
    try:
        b=int(input("Enter first number:"))
        break
    except ValueError:
        print("Your input was not a number")
if choice==1:
    Add()
if choice==2:
    Subtract()
if choice==3:
    Multiply()
if choice==4:
    Divide()
