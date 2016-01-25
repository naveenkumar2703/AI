"""Abstract Class file for  search algorithm."""
#AI HW1
#Authors Naveen & Gowtham

from Distance import *

class DistanceFinder (object):
    def __init__(self, origin, destination,distance_directory):
        self.distance_directory = distance_directory
        self.origin = origin
        self.destination = destination

    #leaving as abstract - to be overridden by child classes
    def searchRoute(self):
        return

    def addToDistance(distance,totalDistanceSofar):
        return totalDistanceSofar + distance.distance()
        
    def removeFromDistance(distance,totalDistanceSofar):
        return totalDistanceSofar - distance.distance()

    def checkIsDestination(self,currentLocation):
        return self.destination == currentLocation

    def printRoute(self):
        route = self.origin

        for city in in_btw_cities:
            route += ', ' + city

        route += ', ' + self.destination
        print route
        
        
