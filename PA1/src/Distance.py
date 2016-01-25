class Distance(object):
    def __init__(self,city1,city2,distance):
        self.city1 = city1
        self.city2 = city2
        self.distance = distance

    def __str__(self):
        return self.city1 + ' is ' + self.distance + 'kms away from' + self.city2
