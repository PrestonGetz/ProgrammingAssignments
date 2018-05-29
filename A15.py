test_array = [5,51,3,3,1,2,89,54,3,5,41,4,65,12,77,321,4]   
dup_items = set()
uniq_items = []
for x in test_array:
   if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
