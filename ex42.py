  class Animal (object):
    pass

## ??
  class Dog (Animal):
  
     def __init__(self, name):
	     ## ??
         self.name = name
		 
## ??
   class Cat (Animal):

   def __init__(self, name):
        ## ??
       	self.name = name

		 
## ??
   class Person(Object):

   def __init__(self, name)		
       ## ??
	   self.name = name 
	   
	   ## Person has a pet of some kind
	   self.pet = none
		 
## ??
   class Employee (Person):

   def __init__(self, name, salary):
   ## ?? hmm, what is this strange magic ?
   super (Employee, self).__init__(name)
   ## ?
   self.salary = salary
   
   		 
## ??
    class Fish (Object):
       pass
	   
## ??
    class Salmon (Fish):
       pass
	 
## ??   
    class Halibut (Fish):
	    pass 

## rover is a dog
rover = dog ("Rover")

## ??
satan = Cat ("Satan")

## ??
mary = Person ("Mary")

## ??
mary.pet = satan

## ??
Frank = Employee  ("Frank ", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish ()

## ??
crouse = Salmon  
 
 ## ??
harry = Halibut ()