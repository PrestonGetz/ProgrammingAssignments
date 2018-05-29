newfile = open("newfile.txt", "w")
num=1
for x in range(11):
  num=num+1
  multiple=1
  newfile.write(str(num)+" TIMES TABLE\n")
  for x in range(12):
    ans=multiple*num
    newfile.write(str(multiple)+" x "+str(num)+" = "+str(ans)+"\n")
    multiple=multiple+1
newfile.close()
