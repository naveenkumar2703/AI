"""Class that implements breadth first search algorithm"""
from DistanceFinder import *
from location import *

class Breadth_First_Finder(DistanceFinder):



    #To be implemented
    def searchRoute(self):
        print 'inside bfs finder'
        if super(Breadth_First_Finder,self).checkIsDestination(self.origin):
            print 'origin is destination'
            super(Breadth_First_Finder,self).printRoute(None)
        else:
            origin_node = location(self.origin,None,self.distance_directory)
            search_tree = [origin_node]
            destination = None
            if not super(Breadth_First_Finder,self).is_dead_end(origin_node):
                #print 'have frontiers'
                #print origin_node.next_location_names
                for node in search_tree:
                    #print node.city
                    if super(Breadth_First_Finder,self).checkIsDestination(node.city):
                        destination = node
                        break
                    else:
                        search_tree.extend(create_next_locations(node, node.next_location_names, self.distance_directory))
                    #print len(search_tree)
                #print 'Destination is:'
                print destination.city

                """self.route = [destination.city]
                parent_city = destination.prev_city
                

                while parent_city.prev_city != None:
                    self.route.append(parent_city.city)
                    parent_city = parent_city.prev_city
                else:
                   self.route.append(parent_city.city)                    

                self.route = list(reversed(self.route))
                print self.route"""
                super(Breadth_First_Finder,self).printRoute(destination)

            else:
                print 'you are in island'
            
        return

def create_next_locations(currentlocation,next_location_names,distance_directory):
    next_locations = []
    for city in next_location_names:
        print 'adding '+city+'with previous city - '+currentlocation.city
        next_location = location(city,currentlocation,distance_directory)
        next_locations.append(next_location)
    currentlocation.state = 'explored'
    print next_locations
    return next_locations

    
