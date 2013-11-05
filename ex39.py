# create a mapping of state to abbreviation
 
states = {
   'Oregon' : 'OR' ,
   'Florida' : 'FL',
   'California' : 'CA',
   'Ney work ' : 'NY' ,     
   'Michigan ' : 'Mi' 
   }

 # create a basic set of states and some cities
 
cities = {
       'CA' : 'San Francisco',
       'MI' : 'Detroit' , 	   
       'FL' :'Jacksonville' 
}

# Add some more cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

#Print out some cities
print '-' * 10
print "NY State has: ", cities ['NY']
print "OR State has: ", cities ['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states ['Michigan']
print "Florida's abbreviation is : ", states ['Florida']

# do it by using the sate then cities dict 
print '-' * 10
print "Michigan has ", cities[states['Michigan']]
print "Florida has ", cities[states['Florida']]
# print every state abbreviation 
print '-' * 10
for state, abbrev in states.items ():
    print "%s is abbreviated %s"% (abbrev, city )
	   
#now do both at the same time 
print '-'* 10
for state, abbrev in states.items ():
    print "%s state is abbreviated %s and has city %s " % (
	    state, abbrev, cities [abbrev])
		
print '-' * 10
# safely get a abbreviation by state the might not be there
state = states.get ('Texas',None)

if not state: 
    print "Sorry, no Texas."

# get a city with default value
city = cities.get ('Tx', 'Does not Exist')
print "The city for the sate 'TX' is: %s " %city