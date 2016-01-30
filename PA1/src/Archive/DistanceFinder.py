"""Abstract Class file for  search algorithm."""
#AI HW1
#Authors Naveen & Gowtham

from Distance import *

class DistanceFinder (object):
    def __init__(self, origin, destination,distance_directory):
        self.distance_directory = distance_directory
        self.origin = origin
        self.destination = destination
        self.route = None

    #leaving as abstract - to be overridden by child classes
    def searchRoute(self):
        return

    def distance_between_cities(self,city1,city2):
        if city1 == city2:
            return 0
        for dist in self.distance_directory.get(city1):
            if dist.city1 == city2 or dist.city2 == city2:
                return dist.distance
                
        return 0
        
    def removeFromDistance(distance,totalDistanceSofar):
        return totalDistanceSofar - distance.distance()

    def checkIsDestination(self,currentLocation):
        return self.destination == currentLocation

    def printRoute(self,destination):
        route = ''
        distance = 0
        from_city = None
        to_city = None

        if self.origin == self.destination:
            self.route = [self.origin,self.destination]
        else:
            self.route = [destination.city]
            parent_city = destination.prev_city
                
            while parent_city.prev_city != None:
                self.route.append(parent_city.city)
                parent_city = parent_city.prev_city
            else:
                self.route.append(parent_city.city)                    

            self.route = list(reversed(self.route))
            #print self.route
                

        for city in self.route:
            route += city + ', '
            if from_city == None:
                from_city = city
            elif to_city == None:
                to_city = city
                distance += int(self.distance_between_cities(from_city,to_city))
                from_city = to_city
                to_city = None
            #else:
                #call calculate dist bwn cities function and swap cities

        route += ' - ' + str(distance)
        print route
        return route

    def is_dead_end(self,location):
        return not len(location.next_location_names) > 0
        
        
