# Create a mapping of state to abbreviation
# Add Oklahoma and Texas to the end of the list.
states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI'}
states ['Oklahoma'] = 'OK'
states ['Texas'] = 'TX'
print(states)
cities = {'CA': 'San Francisco',
          'MI': 'Detroit', 
          'FL': 'Jacksonville'}  
          
#add the rest of the cities here including Oklahoma and Texas
cities ['OK'] = 'Oklahoma City'
cities ['TX'] = 'Houston'
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'
cities ['FL'] = 'Tallahassee'
cities ['CA'] = 'Sacramento'
cities ['MI'] = 'Lansing'

# Print out all the cities
print ('-' * 20)
print ("OK State has: ", cities['OK'])
print ("TX State has: ", cities['TX'])
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])
print ("FL State has: ", cities['FL'])
print ("CA State has: ", cities['CA'])
print ("MI State has: ", cities['MI'])

# Print out all the states
print ('-' * 20)
print ("Oklahoma's abbreviation is: ", states['Oklahoma'])
print ("Texas' abbreviation is: ", states['Texas'])
print ("New York's abbreviation is: ", states['New York'])
print ("Oregon's abbreviation is: ", states['Oregon'])
print ("Florida's abbreviation is: ", states['Florida'])
print ("California's abbreviation is: ", states['California'])
print ("Michigan's abbreviation is: ", states['Michigan'])
