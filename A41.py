a = int(input())
b = int(input())

r=0

def eight():
    c=a+b
    d=a-b
    c1=abs(c)
    d1=abs(d)
    if a==8:
        r=1
    if b==8:
        r=1
    if c1==8:
        r=1
    if d1==8:
        r=1
    if r==1:
        print("true")
eight()
