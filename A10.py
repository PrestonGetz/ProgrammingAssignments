ans = 0
for i in range (0,500):
  if(i % 3 == 0 or i % 5 == 0):
    ans = ans+i
print(ans)
#ans2 = sum(set(list(range(0,500,3)) + list(range(0,500,5))))
#print(ans2) this is faster
