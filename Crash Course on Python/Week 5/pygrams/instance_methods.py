class Piglet:
    def speak(self):
        print("oink oink")
        return self
    
hamlet = Piglet()
print(hamlet.speak())

print("--------------------------------")
class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

hamlet = Piglet()
hamlet.name = "Hamlet"

hamlet.speak()





print("--------------------------------")
petunia = Piglet()
petunia .name = "Petunia"

petunia.speak()

print("--------------------------------")
class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18



print("--------------------------------")
piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())




print("--------------------------------")
class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())


#Constructors and Other Special Methods (Optional)
'''
Want to see this in action? In this code, there's a Person class that has an attribute name, which gets set when constructing the
object. Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 2) when the
greeting() method is called, the greeting states the assigned name.
'''


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ("hi, my name is {}".format(self.name)) 

# Create a new instance with a name of your choice
some_person = Person("Gary")  
# Call the greeting method
print(some_person.greeting())


#Remember our Person class from the last video? Let’s add a docstring to the greeting method. How about, “Outputs a message
# with the name of the person”.

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)

'''
Here is your output:
Help on class Person in module submission:

class Person(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  greeting(self)
 |      Outputs a message with the name of the person
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


Excellent! You’ve mastered the art of providing info using
docstrings!
'''


''''
Documenting Functions, Classes, and Methods (Optional)
'''
def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes, and seconds."""
    return hours*3600+minutes*60+seconds

help(to_seconds)

    
class Fruit:
     def __init__(self, color, flavor):
         self.color = color
         self.flavor = flavor

class Apple(Fruit):
    pass
class Apple(Fruit):
    pass













