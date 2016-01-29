class location(object):
    def __init__(self,city,prev_city,route_dict):
        self.city = city
        self.prev_city = prev_city#this will serve as parent node
        self.next_location_names = get_next_location_names(city,prev_city,route_dict)
        self.next_locations = None
        self.state = 'none'
        
def get_next_location_names(currentcity,prev_city,route_dict):
        nxt_city_lst = []
        
        for dist in route_dict.get(currentcity):
            #print dist
            if prev_city != None and dist.city1 != prev_city.city and dist.city2 != prev_city.city:
                nxt_city_lst.append(get_other_city(dist, currentcity))               
            elif prev_city == None:
                nxt_city_lst.append(get_other_city(dist, currentcity))
        #print nxt_city_lst
        return nxt_city_lst



def get_other_city(distance,currentcity):
    if distance.city1 == currentcity:
        return distance.city2
    elif distance.city2 == currentcity:
        return distance.city1
