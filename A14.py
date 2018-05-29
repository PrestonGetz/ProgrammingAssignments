import time
num = 1
ammount = int(input("What do you want to count to?"))
for i in range(ammount):
  print(num)
  num = num + 1
  time.sleep(1)
