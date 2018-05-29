wordused=input("what is the string?")
lists=list(wordused)
s=input("what do you want to remove")
for x in lists:
  if s in lists:
    lists.remove(s)
print(''.join(lists))
