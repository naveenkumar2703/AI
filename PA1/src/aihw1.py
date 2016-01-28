"""Program for AI programming assignment -1 and home work 2"""
import csv
from Distance import *
from Breadth_First_Finder import *
from Depth_First_Finder import *
from Iterative_Depth_Finder import *
from DistanceFinder import *

def get_input(text_for_user):
    print (text_for_user)
    return raw_input()

def num_exist(string):
    return any(char.isdigit() for char in string)

        

def parse_input_file(cities_list,distance_lookup):
    f = open('distance.csv')
    input_file = csv.reader(f)
    for row in input_file:
        columns_parsed = 0
        city1 = ''
        city2 = ''
        distance = ''
        #print row
        if len(row) > 0:
            
            for column in row:
                #print column
                if columns_parsed == 3:
                    break
                elif len(column) > 0:
                    if (column.lower() not in cities_list) and (not num_exist(column)):
                        cities_list.append(column.lower())
                    if columns_parsed == 0:
                        city1 = column.lower()
                    elif columns_parsed == 1:
                        city2 = column.lower()
                    elif columns_parsed == 2:
                        distance = column
                    columns_parsed += 1
                    
            distance_obj = Distance(city1,city2,distance)
            
            
            if len(city1) > 0 and len(city2) > 0 and len(distance)>0:
                #print distance_obj
                if not city1 in distance_lookup:
                    distance_lookup[city1]=[distance_obj]
                else:
                    #print 'city1-'+city1
                    #print distance_lookup[city1]
                    distance_lookup[city1].append(distance_obj)
                    #print distance_lookup[city1]
                if not city2 in distance_lookup:
                    distance_lookup[city2]=[distance_obj]
                else:
                    #print 'city2'+city2
                    #print distance_lookup[city2]
                    distance_lookup[city2].append(distance_obj)
            
                
    #print distance_lookup
    #print cities_list
    #print len(cities_list)
    return distance_lookup


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
finder = None

if search_method == 'bfs':
    finder = Breadth_First_Finder(city1, city2, distance_lookup)
elif search_method == 'dfs':
    finder = Depth_First_Finder(city1, city2, distance_lookup)
elif search_method == 'ids':
    finder = Iterative_Depth_Finder(city1, city2, distance_lookup)

finder.searchRoute()



    

