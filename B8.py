# Don't delete any of the given code.

count=0
before=''

def countYZ(strings):
    # insert your logic here
    count=0
    before=''
    for character in strings:
        z=character.isalpha()
        if z==False:
            if before=='y' or before=='z':
                count+=1
        before=character.lower()
    if before=='y' or before=='z':
        count+=1
    return count

  
  
# Test cases. Don't modify  
print(1,countYZ("fez day"))   # this would be 2
print(2,countYZ("day fez"))   # this would be 2
print(3,countYZ("day fyyyz"))   # this would be 2
print(4,countYZ("day yak"))    # this would be 1
print(5,countYZ("day:yak"))
print(6,countYZ("!!day--yaz!!"))
print(7,countYZ("yak zak"))
print(8,countYZ("DAY abc XYZ"))
print(9,countYZ("aaz yyz my"))
print(10,countYZ("y2bz"))
print(11,countYZ("zxyx"))
