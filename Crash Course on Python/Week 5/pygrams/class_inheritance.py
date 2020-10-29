'''
Let’s create a new class together and inherit from it. Below we have a base class called Clothing. Together, let’s create a second
class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks to make it work properly.
'''

class Clothing:
    material = ""
    def __init__(self,name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name,self.material))
            
class Shirt(Clothing):
    material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()


print("==============================")
#Composition (Optional)
class Repository:
    def __init__(self):
        self.package = {}
    def add_package(self, package):
        
        self.packages[package.name] = package
    def total_soze(self):
        
        result = 0
        
        for package in self.packages.values():
            result += package.size
        return result
    
    
    
    
    