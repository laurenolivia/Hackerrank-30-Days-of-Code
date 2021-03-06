"""
Objective 
In this challenge, we're going to learn about the difference between a class/ 
and an instance; because this is an Object Oriented concept, it's only enabled/ 
in certain languages. Check out the Tutorial tab for learning materials and an/ 
instructional video!

Task 
Write a Person class with an instance variable, , and a constructor that takes/
an integer, , as a parameter. The constructor must assign  to  after confirming/ 
the argument passed as  is not negative; if a negative argument is passed as ,/ 
the constructor should set  to  and print Age is not valid, setting age to 0../
In addition, you must write the following instance methods:

yearPasses() should increase the  instance variable by .
amIOld() should perform the following conditional actions:

If age < 13, print You are young..

If age >= 13 and age < 18, print You are a teenager..

Otherwise, print You are old..

"""



class Person():
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge     
        if initialAge > 0:
            self.age = initialAge
        else:
            print("Age is not valid, setting age to 0.")
            self.age = 0
      
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
        
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
        