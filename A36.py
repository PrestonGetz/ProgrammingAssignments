import random
one=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
two=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',1,2,3,4,5,6,7,8,9]
three=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',1,2,3,4,5,6,7,8,9,'!','@','#','$','%','^','&','*','(',')','-','_','=','+']
length=int(input('How long do you want your password to be?'))
print('[1]-letters\n[2]-letters and numbers\n[3]-letters, numbers, and symbols')
what=int(input())
password=''
if what==1:
  for x in range(length):
    password+=str(random.choice(one))
elif what==2:
  for x in range(length):
    password+=str(random.choice(two))
elif what==3:
  for x in range(length):
    password+=str(random.choice(three))
print(str(password))



# print the random password.
