class Locality(object):
    
    def __init__(self, name, locality_type, population):
        self.name = name
        self.locality_type = locality_type
        self.population = population

    def get_name(self):
        return self.name

    def get_locality_type(self):
        return self.locality_type

    def __str__(self):
        return "%s is a %s. Its population is %d" % (self.name, self.locality_type, self.population)

class Village(Locality):
    def __init__(self, name, population):
        Locality.__init__(self, name, "village", population)

class Town(Locality):
    def __init__(self, name, population):
        Locality.__init__(self, name, "town", population)

class City(Locality):
    def __init__(self, name, population):
        Locality.__init__(self, name, "city", population)
