"""Program for AI programming assignment -1 and home work 2"""
import csv

def get_input(text_for_user):
    print text_for_user
    return raw_input()

def num_exist(string):
    return any(char.isdigit() for char in string)

class Distance(object):
    def __init__(self,city1,city2,distance):
        self.city1 = city1
        self.city2 = city2
        self.distance = distance

    def __str__(self):
        return self.city1 + ' is ' + self.distance + 'kms away from' + self.city2
        

def parse_input_file(cities_list,distance_lookup):
    f = open('distance.csv')
    input_file = csv.reader(f)
    for row in input_file:
        columns_parsed = 0
        city1 = ''
        city2 = ''
        distance = ''
        print row
        if len(row) > 0:
            
            for column in row:
                print column
                if columns_parsed == 3:
                    break
                elif len(column) > 0:
                    if column not in cities_list and not num_exist(column):
                        cities_list.append(column.lower())
                    if columns_parsed == 0:
                        city1 = column.lower()
                    elif columns_parsed == 1:
                        city2 = column.lower()
                    elif columns_parsed == 2:
                        distance = column
                    columns_parsed += 1
                    
            distance_obj = Distance(city1,city2,distance)
            print city1
            print distance_obj
            if len(city1) > 0 and len(city2) > 0:
                if not city1 in distance_lookup:
                    distance_lookup[city1]=[distance_obj]
                else:
                    print distance_lookup[city1]
                    distance_lookup[city1] = distance_lookup[city1].append(distance_obj)
                if not city2 in distance_lookup:
                    distance_lookup[city2]=[distance_obj]
                else:
                    print distance_lookup[city2]
                    distance_lookup[city2] = distance_lookup[city2].append(distance_obj)
            
                
    print distance_lookup
    print cities_list
    return ""


cities_list = []
distance_lookup = {}

parse_input_file(cities_list,distance_lookup)
city1 = get_input('Enter city 1:').lower()
while(city1 not in cities_list):
    print city1 + ' is not in Romania.'
    city1 = get_input('Enter city 1:').lower()

city2 = get_input('Enter city 2:').lower()

while(city2 not in cities_list):
    print city2 + ' is not in Romania.'
    city2 = get_input('Enter city 2:').lower()


search_method = get_input('Choose a search method: bfs or dfs or ids').lower()

while (search_method not in ['bfs','dfs','ids']):
    print 'Invalid search method!!!'
    search_method = get_input('Choose a search method: bfs or dfs or ids').lower()
print 'Calling:' + search_method + ' algorithm'

#TO DO call respective algorithm by passing in distance_lookup
