import abc

class BusRoute(abc.ABC):
    def __init__(self, name, capacity, trip_duration, stops_count, ticket_price):
        self.name = name
        self.capacity = capacity
        self.trip_duration = trip_duration
        self.stops_count = stops_count
        self.ticket_price = ticket_price

    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def get_trip_duration(self):
        return self.trip_duration

    def get_stops_count(self):
        return self.stops_count

    def get_ticket_price(self):
        return self.ticket_price

    def set_name(self, name):
        self.name = name

    def set_capacity(self, capacity):
        self.capacity = capacity

    def set_trip_duration(self, trip_duration):
        self.trip_duration = trip_duration

    def set_stops_count(self, stops_count):
        self.stops_count = stops_count
    
    def set_ticket_price(self, ticket_price):
        self.ticket_price =- ticket_price

    def delete_attribute(self, attribute_name):
        delattr(self, attribute_name)

    def __str__(self):
        return "Bus route %s has %d capacity. Duration is %d minutes. There are %d stops. The ticket price is %d" % (self.name, self.capacity, self.trip_duration, self.stops_count, self.ticket_price)

kyiv_kherson = BusRoute('Kyiv - Kherson', 500, 800, 10, 200)