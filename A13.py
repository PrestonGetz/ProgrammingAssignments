array=[]
num=int(input("How many elements do you want?"))
for i in range(num):
  numadd=int(input("Enter next number"))
  array.append(numadd)
number=int(input("What number do you want to find?"))
def list_count_numbers(nums):
  count=0  
  for num in nums:
    if num==number:
      count+=1
  return count
print("There are",list_count_numbers(array), str(number),"'s")
