# Robert Muhlestein
# 000936977

from hashmap import HashMap
from distance import Distance
from truck import Truck


def convert_time(time):
    # Big O: O(1)
    # takes the user_input 'time' and converts it into a usable
    # 'elapsed_time'. using 0800 as the zero point
    adjust = int(time) - 800
    minutes = adjust % 100
    hours = int(time[:2]) - 8
    new_hours = int(hours) * 60
    elapsed_time = int(new_hours) + int(minutes)
    return elapsed_time


def combine_lists(list_a, list_b, list_c):
    # Big O: O(N)
    # combine the list of packages assigned to the 3 trucks into 1 list
    # for ease of setting the status of all packages.
    all_packages = []
    for package in list_a:
        all_packages.append(package)
    for package in list_b:
        all_packages.append(package)
    for package in list_c:
        all_packages.append(package)
    return all_packages

def get_delivery_time(m, eta, elapsed_time, start_time, truck):
    for times in eta:
        start_time = times + float(start_time)
        #start_time = int(start_time)
        #print start_time
        new_time = start_time - 800
        if new_time <60:
            delivered_time = start_time
            print"package will be delivered at {}".format(int(delivered_time))
            return delivered_time
        elif new_time < 120:
            delivered_time = start_time + 40
            print"package will be delivered at {}".format(int(delivered_time))
            return delivered_time
        elif new_time < 180:
            delivered_time = start_time +80
            print"package will be delivered at {}".format(int(delivered_time))
            return delivered_time
        elif new_time < 240:
            delivered_time = start_time + 120
            print"package will be delivered at {}".format(int(delivered_time))
            return delivered_time
        elif new_time < 300:
            delivered_time = start_time + 160
            print("package will be delivered at {}".format(int(delivered_time)))
            return delivered_time
        time = elapsed_time
        print time
        time = time - times
        if time > 0:
            index = eta.index(times)
            address = truck[index + 1]
            packages = m.get_package_number(address)
            print packages
            for package in packages:
                notes = m.get_notes(package)
                if "WRONG" in notes.upper():
                    continue
                else:
                    m.set_status_delivered(package)
                    #print('#{} STATUS -- {}'.format(package, m.set_status_delivered(package)))
        else:
            index = eta.index(times)
            print index
            address = truck[index + 1]
            packages = m.get_package_number(address)
            for package in packages:
                status = m.get_status(package)
                print status
                if "DELIVERED" not in status:
                    m.set_status_out_for_delivery(package)
                    #print('#{} STATUS -- {}'.format(package, m.set_status_out_for_delivery(package)))
      

def set_up_status(m, list):
    # Big O: O(N)
    # takes the list of all packages and sets the status of all packages
    # as soon as they reach the hub (unless package is delayed).
    for package in list:
        notes = m.get_notes(package)
        if "DELAYED" in notes.upper():
            m.set_status_delayed(package)
            #print('#{} STATUS -- {}'.format(package, m.set_status_delayed(package)))
        else:
            m.set_status_at_hub(package)
            #print('#{} STATUS -- {}'.format(package, m.set_status_at_hub(package)))
            

def correct_address(m, package_list, new_address):
    # Big O:
    # fixes the address in "WRONG ADDRESS" packages
    new_notes = "ADDRESS CORRECTED"
    new_zipcode = "84111"
    for package in package_list:
        notes = m.get_notes(package)
        if "WRONG ADDRESS" in notes.upper():
            m.set_new_address(package, new_address)
            m.set_new_zipcode(package, new_zipcode)
            m.set_new_notes(package, new_notes)


def send_1(m, elapsed_time, distances, truck):
    # Big O: O(N^2)
    """
    sends truck 1 out for delivery.
    calculates time to each location
    subtracts the time it take to reach a location from the elapsed_time
    if remaining time > 0 set status to package delivered,
    if remaining time < 0 set remaining statuses to out for delivery
    """

    total_1 = 0
    delivery_time = 800
    for distance in distances:
        total_1 = total_1 + distance
    eta = []
    time = elapsed_time
    for distance in distances:
        eta.append(distance / .3)
    #return_time = get_delivery_time(m, eta, elapsed_time, '0800', truck)
    for times in eta:
        time = time - times
        if time > 0:
            delivery_time = int(delivery_time) + int(times)
            index = eta.index(times)
            address = truck[index + 1]
            packages = m.get_package_number(address)
            for package in packages:
                notes = m.get_notes(package)                
                addresss = m.get_address(package)
                if "WRONG" in notes.upper():
                    continue
                else:
                    m.set_status_delivered(package)
                    if delivery_time < 860:
                        print "#{} - {} delivered at {}".format(package, addresss, delivery_time)
                    elif delivery_time < 920:
                        new_time = delivery_time + 40
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 980:
                        new_time = delivery_time + 80
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
        else:
            delivery_time = int(delivery_time) + int(times)
            index = eta.index(times)
            address = truck[index + 1]
            packages = m.get_package_number(address)
            for package in packages:
                status = m.get_status(package)
                addresss = m.get_address(package)
                if "DELIVERED" not in status:
                    m.set_status_out_for_delivery(package)
                    if delivery_time < 860:
                        print "#{} - {} projected delivery at {}".format(package, addresss, delivery_time)
                    elif delivery_time < 920:
                        new_time = delivery_time + 40
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
                    elif delivery_time < 980:
                        new_time = delivery_time + 80
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
    return total_1


def send_2(m, elapsed_time, distances, truck):
    # Big O: O(N^2)
    """
    sends truck 2 out for delivery.
    calculates time to each location
    subtracts the time it take to reach a location from the elapsed_time
    if remaining time > 0 set status to package delivered,
    if remaining time < 0 set remaining statuses to out for delivery
    """

    total_2 = 0
    delivery_time = 905
    for distance in distances:
        total_2 = total_2 + distance
    eta = []
    time = elapsed_time
    for distance in distances:
        eta.append(distance / .3)
    for times in eta:
        time = time - times
        if time > 0:
            delivery_time = int(delivery_time) + int(times)
            index = eta.index(times)
            address = truck[index + 1]
            packages = m.get_package_number(address)
            for package in packages:
                notes = m.get_notes(package)
                addresss = m.get_address(package)
                if "WRONG" in notes.upper():
                    continue
                else:
                    m.set_status_delivered(package)
                    if delivery_time < 960:
                        print "#{} - {} delivered at {}".format(package, addresss, delivery_time)
                    elif delivery_time < 1020:
                        new_time = delivery_time + 40
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 1080:
                        new_time = delivery_time + 80
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 1140:
                        new_time = delivery_time + 120
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
        else:
            delivery_time = int(delivery_time) + int(times)
            index = eta.index(times)
            address = truck[index + 1]
            packages = m.get_package_number(address)
            for package in packages:
                status = m.get_status(package)
                if "DELIVERED" not in status:
                    m.set_status_out_for_delivery(package)
                    if delivery_time < 960:
                        print "#{} - {} projected delivery at {}".format(package, addresss, delivery_time)
                    elif delivery_time < 1020:
                        new_time = delivery_time + 40
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
                    elif delivery_time < 1080:
                        new_time = delivery_time + 80
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
                    elif delivery_time < 1140:
                        new_time = delivery_time + 120
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
    return total_2


def send_3(m, elapsed_time, distances, truck):
    # Big O: O(N^2)
    """
    sends truck 3 out for delivery.
    calculates time to each location
    subtracts the time it take to reach a location from the elapsed_time
    if remaining time > 0 set status to package delivered,
    if remaining time < 0 set remaining statuses to out for delivery
    """

    total_3 = 0
    delivery_time = 1020
    for distance in distances:
        total_3 = total_3 + distance
    eta = []
    time = elapsed_time
    for distance in distances:
        eta.append(distance / .3)
    for times in eta:
        time = time - times
        if time > 0:
            delivery_time = int(delivery_time) + int(times)
            index = eta.index(times)
            address = truck[index + 1]
            packages = m.get_package_number(address)
            for package in packages:
                status = m.get_status(package)
                if "DELIVERED" in status.upper():
                    continue
                else:    
                    m.set_status_delivered(package)
                    addresss = m.get_address(package)
                    if delivery_time < 1060:
                        print "#{} - {} delivered at {}".format(package, addresss, delivery_time)
                    elif delivery_time < 1120:
                        new_time = delivery_time + 40
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 1180:
                        new_time = delivery_time + 80
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 1240:
                        new_time = delivery_time + 120
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 1300:
                        new_time = delivery_time + 160
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 1360:
                        new_time = delivery_time + 200
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 1420:
                        new_time = delivery_time + 240
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
        else:
            delivery_time = int(delivery_time) + int(times)
            index = eta.index(times)
            address = truck[index + 1]
            packages = m.get_package_number(address)
            for package in packages:
                status = m.get_status(package)
                addresss = m.get_address(package)
                if "DELIVERED" not in status:
                    m.set_status_out_for_delivery(package)
                    if delivery_time < 1060:
                        print "#{} - {} projected delivery at {}".format(package, addresss, delivery_time)
                    elif delivery_time < 1120:
                        new_time = delivery_time + 40
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
                    elif delivery_time < 1180:
                        new_time = delivery_time + 80
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
                    elif delivery_time < 1240:
                        new_time = delivery_time + 120
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
                    elif delivery_time < 1300:
                        new_time = delivery_time + 160
                        print "#{} - {} delivered at {}".format(package, addresss, new_time)
                    elif delivery_time < 1360:
                        new_time = delivery_time + 200
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
                    elif delivery_time < 1420:
                        new_time = delivery_time + 240
                        print "#{} - {} projected delivery at {}".format(package, addresss, new_time)
    return total_3


def main():
    m = HashMap()
    m.load_package_details("package_details.txt", m)
    d = Distance()
    d.load_distances('node_list.txt', 'combo.txt', d)
    t = Truck()
    truck_1_packages, truck_2_packages, truck_3_packages = t.prep_trucks()
    all_packages = combine_lists(truck_1_packages, truck_2_packages, truck_3_packages)

    print
    print(42 * "-")
    print("Data Structures and Algorithms 2 - C950")
    print(13 * " " + "Rob Muhlestein")
    print(42 * "-")
    print(30 * '-')
    print(6 * " " + "M A I N - M E N U")
    print(30 * '-')
    print("1. Lookup package details (ID input & Time input")
    print("2. Lookup package details (Address input & Time input")
    print("3. Run Delivery Simulation - Input Time")
    print("4. Print Delivery Report (ID# & Status Only) - Input Time")
    print(30 * '-')

    ## Get Input ###
    choice = raw_input()

    ### Take action as per selected menu-option ##
    if choice == '1':
        # lookup package details (ID and time input)
        print("Preparing Simulation...")
        for packages in all_packages:
            m.retrieve(packages)
        print
        user_time = raw_input("What time would you like to simulate? \n (24 hr format e.g. 0900, 1315): ")
        if len(user_time) != 4 or ":" in user_time:
            # raise error message if time entered is not in a useable format
            raise ValueError(
                "Entry: {} is not a valid entry.\n\tPlease ensure the time you enter is in the format '0000'. E.g. 0900.\n\tDo not include ':' or 'AM' or 'PM'.".format(
                    user_time))
        else:
            if user_time[-2:] > '59':
                # raise error message if time entered isn't a valid time
                raise ValueError('Entry: {} -- minutes > 59 is not a valid time entry.'.format(user_time))
            else:
                inquiry_ID = raw_input("Enter ID#: ")
                elapsed_time = convert_time(user_time)

                if elapsed_time < 65:  # 0905

                    # 0800- all trucks get loaded
                    # Truck 1, having the highest priority packages,
                    # leaves first

                    truck_1 = t.load_truck(m, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    send_1(m, elapsed_time, distances_1, truck_1)

                    print("\nPrinting Package Info for {}".format(inquiry_ID))
                    key, vals = m.retrieve(inquiry_ID)
                    print("{}: {}".format(key, vals))

                    main()

                elif elapsed_time < 140:  # 1020
                    # 0905 Delayed packages arrive
                    # Truck 2 delivers delayed packages
                    # with 1030 deadline first.
                    # Truck 1 should arrive back to the hub @ 1007

                    truck_1 = t.load_truck(m, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    send_1(m, elapsed_time, distances_1, truck_1)

                    start_time = elapsed_time - 65
                    truck_2 = t.load_truck(m, truck_2_packages)
                    distances_2 = d.distance_traveled(elapsed_time, truck_2)
                    send_2(m, start_time, distances_2, truck_2)

                    print("\nPrinting Package Info for {}".format(inquiry_ID))
                    key, vals = m.retrieve(inquiry_ID)
                    print("{}: {}".format(key, vals))

                    main()
                else:
                    # wrong address is corrected
                    # Truck 3 leaves after correction at 1020

                    truck_1 = t.load_truck(m, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    total_1 = send_1(m, elapsed_time, distances_1, truck_1)

                    start_time = elapsed_time - 65
                    truck_2 = t.load_truck(m, truck_2_packages)
                    distances_2 = d.distance_traveled(elapsed_time, truck_2)
                    total_2 = send_2(m, start_time, distances_2, truck_2)

                    start_time = elapsed_time - 140
                    new_address = "410 S State St"
                    correct_address(m, truck_3_packages, new_address)
                    truck_3 = t.load_truck(m, d, truck_3_packages)
                    distances_3 = d.distance_traveled(elapsed_time, truck_3)
                    total_3 = send_3(m, start_time, distances_3, truck_3)

                    print("\nPrinting Package Info for {}".format(inquiry_ID))
                    key, vals = m.retrieve(inquiry_ID)
                    print("{}: {}".format(key, vals))
                
                    main()
    
    elif choice == '2':
        # lookup package details address and time
        print("Preparing Simulation...")
        for packages in all_packages:
            m.retrieve(packages)
        print
        user_time = raw_input("What time would you like to simulate? \n (24 hr format e.g. 0900, 1315): ")
        if len(user_time) != 4 or ":" in user_time:
            # raise error message if time entered is not in a useable format
            raise ValueError(
                "Entry: {} is not a valid entry.\n\tPlease ensure the time you enter is in the format '0000'. E.g. 0900.\n\tDo not include ':' or 'AM' or 'PM'.".format(
                    user_time))
        else:
            if user_time[-2:] > '59':
                # raise error message if time entered isn't a valid time
                raise ValueError('Entry: {} -- minutes > 59 is not a valid time entry.'.format(user_time))
            else:
                inquiry_address = raw_input("Enter Address: ")
                elapsed_time = convert_time(user_time)

                if elapsed_time < 65:  # 0905

                    # 0800- all trucks get loaded
                    # Truck 1, having the highest priority packages,
                    # leaves first

                    truck_1 = t.load_truck(m, d, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    send_1(m, elapsed_time, distances_1, truck_1)

                    print("\nPrinting status for package(s) going to {}".format(inquiry_address))
                    packages = m.get_package_number(inquiry_address)
                    print("{}\t{}\t{}".format(inquiry_address, packages, m.get_status(packages[0])))

                    main()

                elif elapsed_time < 140:  # 1020
                    # 0905 Delayed packages arrive
                    # Truck 2 delivers delayed packages
                    # with 1030 deadline first.
                    # Truck 1 should arrive back to the hub @ 1007

                    truck_1 = t.load_truck(m, d, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    send_1(m, elapsed_time, distances_1, truck_1)

                    start_time = elapsed_time - 65
                    truck_2 = t.load_truck(m, d, truck_2_packages)
                    distances_2 = d.distance_traveled(elapsed_time, truck_2)
                    send_2(m, start_time, distances_2, truck_2)

                    print("\nPrinting status for package(s) going to {}".format(inquiry_address))
                    packages = m.get_package_number(inquiry_address)
                    print("{}\t{}\t{}".format(inquiry_address, packages, m.get_status(packages[0])))

                    main()
                else:
                    # wrong address is corrected
                    # Truck 3 leaves after correction at 1020

                    truck_1 = t.load_truck(m, d, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    total_1 = send_1(m, elapsed_time, distances_1, truck_1)

                    start_time = elapsed_time - 65
                    truck_2 = t.load_truck(m, d, truck_2_packages)
                    distances_2 = d.distance_traveled(elapsed_time, truck_2)
                    total_2 = send_2(m, start_time, distances_2, truck_2)

                    start_time = elapsed_time - 140
                    new_address = "410 S State St"
                    correct_address(m, truck_3_packages, new_address)
                    truck_3 = t.load_truck(m, d, truck_3_packages)
                    distances_3 = d.distance_traveled(elapsed_time, truck_3)
                    total_3 = send_3(m, start_time, distances_3, truck_3)

                    print("\nPrinting status for package(s) going to {}".format(inquiry_address))
                    packages = m.get_package_number(inquiry_address)
                    print("{}\t{}\t{}".format(inquiry_address, packages, m.get_status(packages[0])))
                
                    main()
       
    elif choice == '3':
        print("Preparing Simulation...")
        for packages in all_packages:
            m.retrieve(packages)
        print
        user_time = raw_input("What time would you like to simulate? \n (24 hr format e.g. 0900, 1315): ")
        if len(user_time) != 4 or ":" in user_time:
            # raise error message if time entered is not in a useable format
            raise ValueError(
                "Entry: {} is not a valid entry.\n\tPlease ensure the time you enter is in the format '0000'. E.g. 0900.\n\tDo not include ':' or 'AM' or 'PM'.".format(
                    user_time))
        else:
            if user_time[-2:] > '59':
                # raise error message if time entered isn't a valid time
                raise ValueError('Entry: {} -- minutes > 59 is not a valid time entry.'.format(user_time))
            else:
                elapsed_time = convert_time(user_time)

                if elapsed_time < 65:  # 0905

                    # 0800- all trucks get loaded
                    # Truck 1, having the highest priority packages,
                    # leaves first

                    print('\nloading truck 1...\ntruck 1 departed the hub at 0800\nstatus of packages on truck 1 as of {}...'.format(user_time))
                    truck_1 = t.load_truck(m, d, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    send_1(m, elapsed_time, distances_1, truck_1)

                    print('\ntruck 2 is scheduled to leave the hub at 0905')
                    print("truck 3 is scheduled to leave the hub at 1020")

                    main()

                elif elapsed_time < 140:  # 1020
                    # 0905 Delayed packages arrive
                    # Truck 2 delivers delayed packages
                    # with 1030 deadline first.
                    # Truck 1 should arrive back to the hub @ 1007

                    print('\nloading truck 1...\ntruck 1 departed the hub at 0800\nstatus of packages on truck 1 as of {}...'.format(user_time))
                    truck_1 = t.load_truck(m, d, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    send_1(m, elapsed_time, distances_1, truck_1)

                    print('\nloading truck 2...\ntruck 2 departed the hub at 0905\nstatus of packages on truck 2 as of {}...'.format(user_time))
                    start_time = elapsed_time - 65
                    truck_2 = t.load_truck(m, d, truck_2_packages)
                    distances_2 = d.distance_traveled(elapsed_time, truck_2)
                    send_2(m, start_time, distances_2, truck_2)

                    print("\ntruck 3 is scheduled to leave the hub at 1020")

                    main()
                else:
                    # wrong address is corrected
                    # Truck 3 leaves after correction at 1020

                    print('\nloading truck 1...\ntruck 1 departed the hub at 0800\nstatus of packages on truck 1 as of {}...'.format(user_time))
                    truck_1 = t.load_truck(m, d, truck_1_packages)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    total_1 = send_1(m, elapsed_time, distances_1, truck_1)
                    print("total milage for truck 1: {}".format(total_1))
                    print('\nloading truck 2...\ntruck 2 departed the hub at 0905\nstatus of packages on truck 2 as of {}...'.format(user_time))
                    start_time = elapsed_time - 65
                    truck_2 = t.load_truck(m, d, truck_2_packages)
                    distances_2 = d.distance_traveled(elapsed_time, truck_2)
                    total_2 = send_2(m, start_time, distances_2, truck_2)
                    print("total milage for truck 2: {}".format(total_2))
                    print('\nloading truck 3...\ntruck 3 departed the hub at 1020\nstatus of packages on truck 3 as of {}...'.format(user_time))
                    start_time = elapsed_time - 140
                    new_address = "410 S State St"
                    correct_address(m, truck_3_packages, new_address)
                    truck_3 = t.load_truck(m, d, truck_3_packages)
                    distances_3 = d.distance_traveled(elapsed_time, truck_3)
                    total_3 = send_3(m, start_time, distances_3, truck_3)
                    print("total milage for truck 3: {}".format(total_3))
                    #print("\nPrinting Package Report as of {}...\n".format(user_time))
                    #m.print_all()

                    truck_total = float(total_1) + float(total_2) + float(total_3)
                    print("\nTotal distance traveled by all trucks: {:0.1f}".format(truck_total))
                    print("Last package is delivered at: 1229")

                    main()
                    
    elif choice == '4':
        print("Preparing Simulation...")
        for packages in all_packages:
            m.retrieve(packages)
        print
        user_time = raw_input("What time would you like to simulate? \n (24 hr format e.g. 0900, 1315): ")
        if len(user_time) != 4 or ":" in user_time:
            # raise error message if time entered is not in a useable format
            raise ValueError(
                "Entry: {} is not a valid entry.\n\tPlease ensure the time you enter is in the format '0000'. E.g. 0900.\n\tDo not include ':' or 'AM' or 'PM'.".format(
                    user_time))
        else:
            if user_time[-2:] > '59':
                # raise error message if time entered isn't a valid time
                raise ValueError('Entry: {} -- minutes > 59 is not a valid time entry.'.format(user_time))
            else:
                elapsed_time = convert_time(user_time)

                if elapsed_time < 65:  # 0905

                    # 0800- all trucks get loaded
                    # Truck 1, having the highest priority packages,
                    # leaves first

                    print('\nloading truck 1...\ntruck 1 has the following destinations')
                    truck_1 = t.load_truck(m, truck_1_packages)
                    print(truck_1)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    send_1(m, elapsed_time, distances_1, truck_1)

                    print("\nPrinting Status Report as of {}...\n".format(user_time))
                    m.print_all_status()

                    main()

                elif elapsed_time < 140:  # 1020
                    # 0905 Delayed packages arrive
                    # Truck 2 delivers delayed packages
                    # with 1030 deadline first.
                    # Truck 1 should arrive back to the hub @ 1007
                    
                    print('\nloading truck 1...\ntruck 1 has the following destinations')
                    truck_1 = t.load_truck(m, truck_1_packages)
                    print(truck_1)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    send_1(m, elapsed_time, distances_1, truck_1)

                    print('\nloading truck 2...\ntruck 2 has the following destinations')
                    start_time = elapsed_time - 65
                    truck_2 = t.load_truck(m, truck_2_packages)
                    print(truck_2)
                    distances_2 = d.distance_traveled(elapsed_time, truck_2)
                    send_2(m, start_time, distances_2, truck_2)

                    print("\nPrinting Status Report as of {}...\n".format(user_time))
                    m.print_all_status()

                    main()
                else:
                    # wrong address is corrected
                    # Truck 3 leaves after correction at 1020
                    
                    print('\nloading truck 1...\ntruck 1 has the following destinations')
                    truck_1 = t.load_truck(m, truck_1_packages)
                    print(truck_1)
                    distances_1 = d.distance_traveled(elapsed_time, truck_1)
                    total_1 = send_1(m, elapsed_time, distances_1, truck_1)
                    
                    print('\nloading truck 2...\ntruck 2 has the following destinations')
                    start_time = elapsed_time - 65
                    truck_2 = t.load_truck(m, truck_2_packages)
                    print(truck_2)
                    distances_2 = d.distance_traveled(elapsed_time, truck_2)
                    total_2 = send_2(m, start_time, distances_2, truck_2)
                    
                    print('\nloading truck 3...\ntruck 3 has the following destinations')
                    start_time = elapsed_time - 140
                    new_address = "410 S State St"
                    correct_address(m, truck_3_packages, new_address)
                    truck_3 = t.load_truck(m, d, truck_3_packages)
                    print(truck_3)
                    distances_3 = d.distance_traveled(elapsed_time, truck_3)
                    total_3 = send_3(m, start_time, distances_3, truck_3)

                    print("\nPrinting Status Report as of {}...\n".format(user_time))
                    m.print_all_status()

                    print("\nDay ends at: 1312")
                    print("Total distance traveled by all trucks at 1312: {}".format(
                        float(total_1) + float(total_2) + float(total_3)))

                    main()
    else:

        print("\n======= Invalid Selection. Please try again. ========")
        print("   ================= select [1-3] =================\n")
        main()



main()
