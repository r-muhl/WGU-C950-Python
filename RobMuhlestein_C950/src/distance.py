from hashmap import HashMap
# Manages distances between each address
# using the HashMap and other lists to manage
# addresses and distances separately
# once each list is completed, the lists are
# combined into a dictionary, which stores the data in
# an easy to access format (key = address, values = distance to each address)

class Distance:
    def __init__(self):
        self.address = HashMap()
        self.distance = []
        self.address_manager = []
        self.combo = {}

    def add_address(self, address, zip_code):
        # Big O: O(1)
        # inserts address into address list
        self.address.insert(address, zip_code)

    def print_addresses(self):
        # Big O: O(1)
        # keys to address list
        self.address.keys()

    def add_distance(self, distance):
        # Big O: O(1)
        # appends distance to list
        self.distance.append(distance)

    def combine(self):
        # Big O: O(N^2)
        # combines the two separate lists (addresses and distances)
        # into a usable dictionary
        keys = self.address.keys()
        distances = self.distance
        for i in keys:
            for j in distances:
                if i in j:
                    del j[0]
                    self.combo[i] = j
        return self.combo

    def distances_from_address(self, address):
        # Big O: O(1)
        # return all distances from address
        return self.combo[address]

    def distance_to_specific(self, address_a, index_b):
        # Big O: O(1)
        # Retrieve the distance between two addresses
        return float(self.combo[address_a][index_b - 1])

    def manage_address(self, address):
        # Big O: O(1)
        # appends address to an address list
        self.address_manager.append(address)
        return self.address_manager

    def index_to_address(self, index):
        # Big O: O(1)
        # finds the address associated with an index
        return self.address_manager[index]

    def address_to_index(self, address):
        # Big O: O(N)
        index_number = 0
        for i in self.address_manager:
            index_number += 1
            if i == address:
                return index_number

    def closest_neighbor(self, address):
        # Big O: O(N)
        # return index # of closest distance
        testing = []
        for i in self.combo[address]:
            testing.append(float(i))
        m = min(i for i in testing if i > 0)
        min_index = testing.index(m)
        closest = self.index_to_address(min_index)
        print('Between {} and {} is {}'.format(address, closest, m))

    def distance_traveled(self, time, list):
        # Big O: O(N)
        # calculates the distances between each address in the list
        # returns the distances in list form
        a = list
        distance_between = []
        for i, nexti in zip(a, a[1::]):
            next_index = self.address_to_index(nexti)
            distance_between.append(self.distance_to_specific(i, next_index))
        return distance_between

    def load_distances(self, node_list, combo, distances):
        # Big O: O(N)
        # read files, sets up addresses and distances between each address
        with open(node_list) as set_address:
            for line in set_address:
                line = line.strip().split('\t')
                distances.add_address(line[0], line)
                distances.manage_address(line[0])
        with open(combo) as set_distance:
            for line in set_distance:
                split = line.strip().split('\t')
                distances.add_distance(split)
        distances.combine()
