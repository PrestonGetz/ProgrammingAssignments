#This program will take an input and give you the coded version
alphabet='abcdefghijklmnopqrstuvwxyz'
key=int(input("What is the key?"))
message=input("Please input a message: ")
newmessage=''
for character in message:
  if character in alphabet:
    position=alphabet.find(character)
    newposition=position+key
    newposition=(position+key)%26
    newcharacter=alphabet[newposition]
    newmessage+=newcharacter
  else:
    newmessage+=character
print("Your message with the key "+str(key)+" is: "+newmessage)
