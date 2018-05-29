# Example code showing how to define a dictionary and add a new key/value pair to it
#person = {'name': 'Bob', 'dob': '12/03/1975', 'gender':'male'}
#person['height'] = 74
#print(person)

# Example code showing how to iterate over the keys and values in a dictionary
#for key in person:
    #print(key, ":", person[key])

# >>>>>>>>>>  END OF EXAMPLES <<<<<<<<<<<<

# Write your solution for Exercises 1 and 2 below here:
me={'Name':'Preston','dob':'21/03/2000','Height':'65','Eye color':'brown',}
for key in me:
    print(key, ":", me[key])

# Write your solution for Exercise 3 below here:
me['Name']='Preston Scott Getz'
# Write your solution for Exercise 4 below here:
me['Shoe size']='10.5'
# Write your solution for Exercise 5 below here:
del me['Eye color']
print('')
print('')
for key in me:
    print(key, ":", me[key])
