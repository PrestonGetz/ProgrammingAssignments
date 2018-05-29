# Don't delete any of the given code.
def round_sum(a, b, c):
    # insert your logic here
    d=a+b+c
    e=[]
    for number in d:
        e.append(number)
    if e[-1]<5:
        e[-1]=0
    if e[-1]>=5:
        e[-1]=0
        e[-2]+=1
        if e[-2]=10:
            
  
  
  
# Test cases. Don't modify  
print(1,'|',round_sum(16, 17, 18))   # this would be 60
print(2,'|',round_sum(12, 13, 14))   # this would be 30
print(3,'|',round_sum(6, 4, 4))      # this would be 10
print(4,'|',round_sum(4, 6, 5))
print(5,'|',round_sum(4, 4, 6))   
print(6,'|',round_sum(9, 4, 4))
print(7,'|',round_sum(0, 0, 1))   
print(8,'|',round_sum(0, 9, 0))
print(9,'|',round_sum(10, 10, 19))   
print(10,'|',round_sum(20, 30, 40))
print(11,'|',round_sum(45, 21, 30))   
print(12,'|',round_sum(23, 11, 26))
print(13,'|',round_sum(10, 10, 19))   
print(14,'|',round_sum(23, 24, 25))
print(15,'|',round_sum(25, 24, 29))   
print(16,'|',round_sum(11, 24, 36))
print(17,'|',round_sum(24, 36, 32))   
print(18,'|',round_sum(14, 12, 26))
print(19,'|',round_sum(12, 10, 24))
