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

class AdministrativeDivision(object):
    def __init__(self, name, administrative_division_type, units):
        self.name = name
        self.administrative_division_type = administrative_division_type
        self.units = units

class TerritorialCommunity(AdministrativeDivision):
    def __init__(self, name, localities=[]):
        AdministrativeDivision.__init__(self, name, "territorial_community", localities)

class District(AdministrativeDivision):
    def __init__(self, name, localities=[]):
        AdministrativeDivision.__init__(self, name, "district", localities)

class Region(AdministrativeDivision):
    def __init__(self, name, districts=[]):
        AdministrativeDivision.__init__(self, name, "region", districts)

class Country(AdministrativeDivision):
    def __init__(self, name, regions=[]):
        AdministrativeDivision.__init__(self, name, "country", regions)