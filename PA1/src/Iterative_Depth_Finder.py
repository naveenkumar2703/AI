"""Class that implements breadth first search algorithm"""
from DistanceFinder import *
from location import *

class Iterative_Depth_Finder(DistanceFinder):
    def __init__(self,origin,destination,distance_directory,depthlimit):
        DistanceFinder.__init__(self,origin,destination,distance_directory)
        self.depthlimit = depthlimit
        

    #To be implemented
    def searchRoute(self):
        print 'inside ids finder'
        if super(Iterative_Depth_Finder,self).checkIsDestination(self.origin):
            print 'origin is destination'
            super(Iterative_Depth_Finder,self).printRoute(None)
        else:
            origin_node = location(self.origin,None,self.distance_directory)
            destination = None
            #first_iter = True
            if not super(Iterative_Depth_Finder,self).is_dead_end(origin_node):
                depth = 0
                while destination == None:
                    destination =  self.explore_child_nodes(origin_node,0,depth+int(self.depthlimit))
                    depth += int(self.depthlimit)                    
                super(Iterative_Depth_Finder,self).printRoute(destination)                

            else:
                print 'you are in island'
            
        return

    def explore_child_nodes(self,node,depth,limit):
        destination = None        
        for option in node.next_location_names:
            #print 'Exploring option: '+option+' - from parent node: '+ node.city + ' Index - '+str(depth)+'limit - '+str(limit)
            option_node = location(option,node,self.distance_directory)
            
            
            if int(depth) >= int(limit):
                return None
            elif super(Iterative_Depth_Finder,self).checkIsDestination(option_node.city):
                return option_node
                
            elif (not super(Iterative_Depth_Finder,self).is_dead_end(option_node)):
                destination = self.explore_child_nodes(option_node,depth+1, limit)
                if destination != None:
                    return destination
                


