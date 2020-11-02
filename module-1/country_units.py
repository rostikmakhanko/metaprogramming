import abc

class Locality(abc.ABC):
    def __init__(self, name, locality_type, population):
        self.name = name
        self.locality_type = locality_type
        self.population = population

    def get_name(self):
        return self.name

    def get_locality_type(self):
        return self.locality_type

    def is_village(self):
        return self.locality_type == "village"

    def is_town(self):
        return self.locality_type == "town"

    def is_city(self):
        return self.locality_type == "city"

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

class AdministrativeDivision(abc.ABC):
    def __init__(self, name, administrative_division_type, units):
        self.name = name
        self.administrative_division_type = administrative_division_type
        self.units = units

    @abc.abstractmethod
    def get_population(self):
        return

    @abc.abstractmethod
    def get_localities_count_by_type(self, locality_type):
        return
        

class TerritorialCommunity(AdministrativeDivision):
    def __init__(self, name, localities=[]):
        AdministrativeDivision.__init__(self, name, "territorial_community", localities)
    
    def get_population(self):
        population = 0
        for locality in self.units:
            population += locality.population
        return population

    def get_localities_count_by_type(self, locality_type):
        localities_count = 0
        for locality in self.units:
            if (locality.locality_type == locality_type):
                localities_count += 1
        return localities_count

class District(AdministrativeDivision):
    def __init__(self, name, localities=[]):
        AdministrativeDivision.__init__(self, name, "district", localities)

    def get_population(self):
        population = 0
        for locality in self.units:
            population += locality.population
        return population

    def get_localities_count_by_type(self, locality_type):
        localities_count = 0
        for locality in self.units:
            if (locality.locality_type == locality_type):
                localities_count += 1
        return localities_count

class Region(AdministrativeDivision):
    def __init__(self, name, districts=[]):
        AdministrativeDivision.__init__(self, name, "region", districts)

    def get_population(self):
        population = 0
        for district in self.units:
            population += district.get_population()
        return population
    
    def get_localities_count_by_type(self, locality_type):
        localities_count = 0
        for districts in self.units:
            localities_count += districts.get_localities_count_by_type(locality_type)
        return localities_count

class Country(AdministrativeDivision):
    def __init__(self, name, regions=[]):
        AdministrativeDivision.__init__(self, name, "country", regions)

    def get_population(self):
        population = 0
        for region in self.units:
            population += region.get_population()
        return population

    def get_localities_count_by_type(self, locality_type):
        localities_count = 0
        for region in self.units:
            localities_count += region.get_localities_count_by_type(locality_type)
        return localities_count