class location(object):
    def __init__(self,city,prev_city,route_dict):
        self.city = city
        self.prev_city = prev_city
        self.route_dict = route_dict
        self.next_city = construct_path(city,prev_city,route_dict)
    def construct_path(city,prev_city,route_dict):
        nxt_city_lst = route_dict.get(city, default = "none")
        nxt_city_lst.remove(prev_city)
        return nxt_city_lst
