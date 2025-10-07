import math

class Particle:
    """Class to store  particles' data in natural units (c=1)"""

    def __init__(self, name, mass, charge, momentum = 0):

        """Attributes of the class:
        -name of the particle 
        -mass in MeV
        -charge in units of e
        -momentum [optional] in Mev
        """
        self._name = name 
        self._mass = mass
        self._charge = charge
        self.momentum = momentum 

    # Encapsulation: make attributes private and 
    # provide property/setter to access and control them
    @property   
    def name(self):
        return self._name
    
    @property   
    def mass(self):
        return self._mass
        
    @property   
    def charge(self):
        return self._charge
         
    @property   
    def momentum(self):
        return self._momentum
    
    @momentum.setter
    def momentum(self, value):
        if value < 0:
            print("Momentum must be positive")
            print("It will be set to zero instead")
            self._momentum = 0
        else:
            self._momentum = value

    @property   
    def energy(self): 
        """Using Einstein formula E = sqrt (m^2 + p^2)"""
        return math.sqrt(self.mass**2 + self.momentum**2)
    
    @energy.setter
    def energy(self, value):
        if value < self.mass:
            print(f"Cannot set energy value to a value lower than the particle mass {self.mass}")
        else:
            self.momentum = math.sqrt(value**2 - self.mass**2) 

    @property
    def beta(self):
        return self.momentum / self.energy
    
    @beta.setter
    def beta(self, value):
        if (value <0 or value > 1):
            print("Invalid Input: beta must take a value between 0 and 1 ")
        elif (value == 1 and self.mass != 0):
            print("Only massless particles can have Beta = 1")   
        else:
            self.momentum = value * self.mass / math.sqrt(1 - value**2)

    """Print particle information in a readable format"""
    def info(self):
        print(f"Particle: {self.name}, mass: {self.mass} Mev, charge: {self.charge} e, momentum: {self.momentum:.2f} Mev")

#Inheritance of Particle class and use class attributes 
class Proton(Particle):
    NAME = "Proton"
    MASS = 938.3 #Mev
    CHARGE = +1 #e
    def __init__(self,momentum=0):
        super().__init__(self.NAME,self.MASS, self.CHARGE, momentum)

class Alfa(Particle):
    NAME = "Alfa"
    MASS = 3727.3 #Mev
    CHARGE = +4 #e
    def __init__(self,momentum=0):
        super().__init__(self.NAME,self.MASS, self.CHARGE, momentum)        



#######################



# Testing Particle and Proton classes
muon = Particle(name = "Muon", mass = 105.6, charge = -1, momentum=-100)
muon.info()
muon.beta = 1
muon.beta = 0.5
muon.info()
muon.momentum = -100

p = Proton()
p.info()
