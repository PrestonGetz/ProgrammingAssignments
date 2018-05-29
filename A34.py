from decimal import Decimal

the_number=0
for x in range(0,100):
  the_number+=1
  number3=the_number/3
  number5=the_number/5
  check3=Decimal(number3)%1==0
  check5=Decimal(number5)%1==0
  if check3 and check5==True:
    print("Trick or Treat!")
  else:
    if check3==True:
      print("trick")
    elif check5==True:
      print("treat")
    else:
      print(str(the_number))
