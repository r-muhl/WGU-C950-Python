from hashmap import HashMap
from distance import Distance


class Truck:
    def __init__(self):
        # lists for holding truck's assigned #
        self.truck_1 = []
        self.truck_2 = []
        self.truck_3 = []
        # sets capacity for trucks
        self.capacity = 16
        # self.distances = Distance()

    def prep_trucks(self):
        # Big O: O(N^2)
        h = HashMap()

        # temporary lists to manage addresses
        truck2_addresses = []
        deadline_addresses = []
        delayed_addresses = []
        delivered_with_addresses = []
        other_addresses = []

        # temporary lists to manage packages
        truck2_packages = []
        deadline_packages = []
        delayed_packages = []
        delivered_with_packages = []
        other_packages = []

        # loads package details for easy assigning and sorting packages
        h.load_package_details("package_details.txt", h)

        # begins the assigning process
        for item in h.items():
            # only applies to the packages that aren't already
            # on a truck or delivered
            if "ON TRUCK" or "DELIVERED" not in item[7]:
                # If it has a deadline (i.e. does not say "EOD" in deadline)
                # this will add it to a separate list
                if "EOD" not in item[4].upper():
                    if item[0] not in deadline_addresses:
                        deadline_addresses.append(item[0])
                # If notes says it must be on truck 2
                # this will add it to a separate list
                if "TRUCK" in item[6].upper():
                    if item[0] not in truck2_addresses:
                        truck2_addresses.append(item[0])
                # If notes says it is delayed
                # this will add it to a separate list
                if "DELAYED" in item[6].upper():
                    if item[0] not in delayed_addresses:
                        delayed_addresses.append(item[0])
                # if notes says it needs to be delivered with ...
                # this will add it to a separate list
                if "DELIVERED WITH" in item[6].upper():
                    a = [int(s) for s in item[6].split() if s.isdigit()]
                    for number in a:
                        if number not in delivered_with_addresses:
                            address = h.get_address(str(number))
                        if address not in delivered_with_addresses:
                            delivered_with_addresses.append(address)
                    if item[0] not in delivered_with_addresses:
                        delivered_with_addresses.append(item[0])
                # this makes a list for everything else
                # without a deadline or without any notes
                if "EOD" in item[4].upper() or "NA" in item[6].upper():
                    if item[0] not in other_addresses:
                        other_addresses.append(item[0])

                # if any overlaps occur between "truck 2", "deadline", or "other"
                # sets priority to truck 2
                for address in truck2_addresses:
                    if address in deadline_addresses:
                        deadline_addresses.remove(address)
                    if address in other_addresses:
                        other_addresses.remove(address)

                # if any overlaps occur between "delayed", "deadline", or "other"
                # sets priority to delayed
                for address in delayed_addresses:
                    if address in deadline_addresses:
                        deadline_addresses.remove(address)
                    if address in other_addresses:
                        other_addresses.remove(address)

                # if any overlaps occur between "delivered with", "deadline", or "other"
                # set priority to delivered_with_addresses
                for address in delivered_with_addresses:
                    if address in deadline_addresses:
                        deadline_addresses.remove(address)
                    if address in other_addresses:
                        other_addresses.remove(address)

                # if any overlaps occur between deadline and "other"
                # set priority to deadline_addresses
                for address in deadline_addresses:
                    if address in other_addresses:
                        other_addresses.remove(address)

        # gets package IDs for addresses assigned to specific lists
        truck2_packages = self.reform_list(h, truck2_addresses)
        deadline_packages = self.reform_list(h, deadline_addresses)
        delayed_packages = self.reform_list(h, delayed_addresses)
        delivered_with_packages = self.reform_list(h, delivered_with_addresses)
        other_packages = self.reform_list(h, other_addresses)

        # sends each list through a double check function finding
        # and finds any with "wrong address" and assigns them to truck 3
        new_truck2 = self.double_check(h, truck2_packages)
        new_deadline = self.double_check(h, deadline_packages)
        new_delayed = self.double_check(h, delayed_packages)
        new_delivered_with = self.double_check(h, delivered_with_packages)
        new_other = self.double_check(h, other_packages)

        # merges package lists, assigns list to trucks
        self.truck_1_packages(h, new_deadline, new_delivered_with)
        self.truck_2_packages(h, new_truck2, new_delayed)
        self.truck_3_packages(h, new_other)

        return self.truck_1, self.truck_2, self.truck_3

    def load_truck(self, m, d, package_list):
        # Big O: O(N)
        # retrieves address for packages, sorts address (attempt to minimize distance traveled),
        # inserts "HUB" as first and last item in list (start and finish at the HUB)
        
        tour = []
        unvisited = []
        
        for package in package_list:
            address = m.get_address(package)
            if address not in unvisited:
                unvisited.append(address)
        last = "HUB"
        while unvisited > []:
            destination = self.sort_lists(d, last, unvisited)
            tour.append(destination)
            unvisited.remove(destination)
            last = destination
        tour.append("HUB")
        tour.insert(0, "HUB")
        return tour

    def sort_lists(self, d, last, unvisited):
        indexes = []
        for address in unvisited:
            ind = d.address_to_index(address)
            indexes.append(ind)
        distances = []
        for index in indexes:
            dist = d.distance_to_specific(last, index)
            distances.append(dist)
        m = min(i for i in distances if i > 0 )
        min_index = distances.index(m)
        closest = unvisited[min_index]
        return closest


    def truck_1_packages(self, h, deadline_packages, deliver_with_packages):
        # Big O: O(N)
        # merges list, assigns to truck 1, triple checks for wrong address
        for package in deadline_packages:
            notes = h.get_notes(str(package))
            if "WRONG ADDRESS" in notes.upper():
                deadline_packages.remove(package)
            self.truck_1.append(package)
        for package in deliver_with_packages:
            notes = h.get_notes(str(package))
            if "WRONG ADDRESS" in notes.upper():
                deadline_packages.remove(package)
            self.truck_1.append(package)
        return self.truck_1

    def truck_2_packages(self, h, truck2_packages, delayed_packages):
        # Big O: O(N)
        # merges list, assigns to truck 2, triple checks for wrong address
        for package in truck2_packages:
            notes = h.get_notes(str(package))
            if "WRONG ADDRESS" in notes.upper():
                truck2_packages.remove(package)
            self.truck_2.append(package)
        for package in delayed_packages:
            notes = h.get_notes(str(package))
            if "WRONG ADDRESS" in notes.upper():
                delayed_packages.remove(package)
            self.truck_2.append(package)
        return self.truck_2

    def truck_3_packages(self, h, other):
        # Big O: O(N)
        # assigns list to truck 3
        for package in other:
            self.truck_3.append(package)
        return self.truck_3

    def reform_list(self, h, address_list):
        # Big O: O(N^2)
        # gets package IDs from addresses
        package_list = []
        for address in address_list:
            pack = h.get_package_number(address)
            package_list.append(pack)
        package_list = [j for i in package_list for j in i]
        return package_list

    def double_check(self, h, package_list):
        # Big O: O(N)
        # finds the specific package that's delayed or has a wrong address
        # and removes them from the truck
        for package in package_list:
            notes = h.get_notes(str(package))
            if "WRONG ADDRESS" in notes.upper():
                package_list.remove(package)
                self.truck_3.append(package)
        return package_list

    def check_capacity(self, h, p, truck):
        # Big O: O(N)
        # double check list length. if length > 16 loops to keep deleting
        # last package until length < 16
        truck_addresses = []
        truck_packages = []
        if len(truck) > 16:
            for package in truck:
                info = h.retrieve(package)
                if info[0] not in truck_addresses:
                    truck_addresses.append(info[0])
            del truck_addresses[-1:]
            for address in truck_addresses:
                truck_packages.append(p.packages_to_address(address))
            truck_packages = [j for i in truck_packages for j in i]
            print(truck_addresses)
            print(truck_packages)
            self.check_capacity(h, p, truck_packages)
        return truck_packages
