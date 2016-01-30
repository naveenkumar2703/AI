"""Class that implements breadth first search algorithm"""
from DistanceFinder import *
from location import *

class Depth_First_Finder(DistanceFinder):

    #To be implemented
    def searchRoute(self):
        if super(Depth_First_Finder,self).checkIsDestination(self.origin):
            print 'origin is destination'
            super(Depth_First_Finder,self).printRoute(None)
        else:
            origin_node = location(self.origin,None,self.distance_directory)
            #search_tree = [origin_node]
            destination = None
            if not super(Depth_First_Finder,self).is_dead_end(origin_node):
               destination =  self.explore_child_nodes(origin_node)
               super(Depth_First_Finder,self).printRoute(destination)                

            else:
                print 'you are in island'
            
        return self.route

    def explore_child_nodes(self,node):
        destination = None
        for option in node.next_location_names:
            #print 'Exploring option: '+option+' - from parent node: '+ node.city
            option_node = location(option,node,self.distance_directory)
            if super(Depth_First_Finder,self).checkIsDestination(option_node.city):
                return option_node
                
            elif not super(Depth_First_Finder,self).is_dead_end(option_node):
                return self.explore_child_nodes(option_node)
