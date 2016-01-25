"""Program for AI programming assignment -1 and home work 2"""


def get_input(text_for_user):
    print text_for_user
    return raw_input()

def parse_input_file():
    f= open('input_file/cities_distance','r')
    print f
    
parse_input_file()
city1 = get_input('Enter city 1:')
city2 = get_input('Enter city 2:')
search_method = get_input('Choose a search method: bfs or dfs or ids')

print city1+city2+search_method
