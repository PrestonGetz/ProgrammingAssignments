word = input("In: ")
consonants=0
for x in word:
    if x=='a'or x=='e'or x =='i'or x=='o'or x=='u':
        placetaker=''
    else:
        consonants+=1
print("There are",str(consonants),"consonants in",word)
