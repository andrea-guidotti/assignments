import math

class Particle:

    def __init__(self, name, mass, charge, momentum = 0):

        self._name = name
        self._mass = mass
        self._charge = charge
        self.momentum = momentum #Mev 

    @property   
    def name(self):
        return self._name
    
    @property   
    def charge(self):
        return self._charge
         
    @property   
    def momentum(self):
        return self._momentum
    
    @momentum.setter
    def momentum(self,momentum):
        if momentum < 0:
            print("Momentum must be positive")
            print("It will be set to zero instead")
            self._momentum = 0
        else:
            self._momentum = momentum

    @property   
    def mass(self):
        return self._mass
    
    @property   
    def energy(self):
        # Using natural units c = 1
        return math.sqrt(self.mass **2 +self.momentum**2)
    
    @energy.setter
    def energy(self, energy):
        if energy < self.mass:
            print(f"Cannot set energy value to a value lower than the particle mass {self.mass}")
        else:
            self.momentum = math.sqrt(self.energy**2 - self.mass**2) 

    @property
    def beta(self):
        return self.momentum / self.energy
    
    @beta.setter
    def beta(self, beta):
        if (beta <0 or beta > 1):
            print("Invalid Input: beta must take a value between 0 and 1 ")
        else:
            self.momentum = beta * self.mass / math.sqrt(1-beta**2)

    def print_info(self):
        print(f"Particle: {self.name}, mass: {self.mass}, charge: {self.charge}, momentum: {self.momentum}")



#######################


muon = Particle(name = "Muon", mass = 105.6, charge = -1, momentum=-100)
print(muon.energy)
muon.print_info()
muon.momentum = -100

