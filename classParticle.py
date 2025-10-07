import math

class Particle:

    def __init__(self, name, mass, charge, momentum = 0):

        self.name = name
        self.mass = mass
        self. charge = charge 
        self.momentum = momentum #Mev 
        
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

    def print_info(self):
        print(f"Particle: {self.name}, mass: {self.mass}, charge: {self.charge}, momentum: {self.momentum}")



#######################


muon = Particle(name = "Muon", mass = 105.6, charge = -1)
print(muon.energy)
muon.print_info()

