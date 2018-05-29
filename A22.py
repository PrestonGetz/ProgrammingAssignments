squares=[]
num_arrays = int(input("How many arrays do you want to find the average of?"))
for x in range(num_arrays):
  a = [int(x) for x in input().split()]
  squares.append((sum(a)/len(a)))
print(squares)
