# hold package details {id: [address, city, state, zip code, deadline, weight, notes, status]}


class HashMap:
    # The hashmap uses a "list of lists" approach using the built-in hash()
    # method. The time commitment is proportional to the number of items
    # that are searched in the buckets - O(N) runtime.
    # By adjusting the number of buckets the runtime can be effected.
    # Increasing and decreasing the bucket number will respectively increase
    # and decrease the runtime. (An increased number of buckets
    # will require more memory).
    def __init__(self):
        self.hashmap = [[] for i in range(256)]

    def _get_hash(self, key):
        return hash(key) % len(self.hashmap)

    def insert(self, key, value):
        # search through hashmap for key
        # if the key exists, update it
        # if not, create a new key
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                break
        if key_found:
            bucket_list[i] = ((key, value))
        else:
            bucket_list.append((key, value))

    def retrieve(self, key):
        # The overall runtime of the application is insignificantly
        # effected due to the nature of hash maps. By hashing the package ID,
        # then searching (linearly) each bucket until the correct package
        # ID is found, we maintain an O(N) runtime. The consumed time would
        # be linearly proportion to the number of buckets searched.
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                # print ("{}: {} ".format(key, v))
                return key, v
        if key_found is not True:
            print("Invalid key. Key matching {} was not found\n".format(key))

    def remove(self, key):
        # search through hashmap for key
        # if the key exists, delete it
        # if not, "not found" message
        key_hash = self._get_hash(key)
        bucket_list = self.hashmap[key_hash]
        key_found = False
        for i in range(0, len(bucket_list)):
            if bucket_list[i][0] == key:
                self.hashmap[key_hash].pop(i)
                key_found = True
        if key_found is not True:
            print("Invalid key. Key matching {} was not be found.".format(key))

    def print_all_status(self):
        # Big O: O(N^2)
        # print status of all packages
        for bucket in self.hashmap:
            for kv in bucket:
                k, item = kv
                print("{}: {}".format(k, item[7]))

    def print_all(self):
        # Big O: O(N^2)
        # print all key- value pairs in the hashmap
        for bucket in self.hashmap:
            for kv in bucket:
                k, item = kv
                print("{}: {}".format(k, item))

    def items(self):
        # Big O: O(N^2)
        # return values only
        items = []
        for bucket in self.hashmap:
            for kv in bucket:
                k, item = kv
                items.append(item)
        return items

    def keys(self):
        # Big O: O(N^2)
        # return keys only
        keys = []
        for bucket in self.hashmap:
            for kv in bucket:
                key, i = kv
                keys.append(key)
        return keys

    def load_package_details(self, file_path, hashmap):
        # Big O: O(N)
        # reads file, inserts each line read into the hashmap as new key- value pairs
        # adds a status to each package

        with open(file_path) as use:
            for line in use:
                id_num, address, city, state, zip_code, deadline, weight, notes = line.split(', ')
                hashmap.insert(id_num,
                               [address, city, state, zip_code, deadline, weight, notes.strip('\n'), "BOUND FOR HUB"])

    ### Setters for package status
    ### Upon file-import, the status is set at "BOUND FOR HUB"
    ### The following will change the status to
    ### "DELAYED", "AT HUB", "LOADED", "OUT FOR DELIVERY" and "DELIVERED"

    def set_status_delayed(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, sets status to "delayed"
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                v[7] = "DELAYED"
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[7]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    def set_status_at_hub(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, sets status to "at hub"
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                v[7] = "AT HUB"
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[7]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    def set_status_loaded(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, sets status to "loaded"
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                v[7] = "LOADED"
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[7]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    def set_status_out_for_delivery(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, sets status to "out for delivery"
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                v[7] = "OUT FOR DELIVERY"
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[7]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    def set_status_delivered(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, sets status to "delivered"
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                v[7] = "DELIVERED"
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[7]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))
            
    def set_new_address(self, key, new_address):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, sets address to new_address
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                v[0] = new_address
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[0]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))
    
    def set_new_zipcode(self, key, new_zipcode):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, sets zipcode to new_zipcode
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                v[3] = new_zipcode
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[3]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))
            
    def set_new_notes(self, key, new_notes):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, sets address to new_address
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                v[6] = new_notes
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[6]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    ### Getters for specific pieces of data needed
    ### such as the address, status, notes, deadline and package ID
    ### Notes and deadlines will be used to set priority

    def get_address(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, returns the address associated with that key
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                return v[0]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    def get_deadline(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, returns the address associated with that key
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                return v[4]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    def get_notes(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, returns the notes & deadline associated with that key
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                return v[6]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    def get_status(self, key):
        # Big O: O(N)
        # searches hashmap for package ID (key)
        # once found, returns status associated with that package
        hash_key = self._get_hash(key)
        bucket_list = self.hashmap[hash_key]
        key_found = False
        for i, kv in enumerate(bucket_list):
            k, v = kv
            if key == k:
                key_found = True
                # print("#{}: STATUS -- {}".format(key, v[7]))
                return v[7]
        if key_found is not True:
            print("Invalid key. Key matching {} was not found".format(key))

    def get_package_number(self, address):
        # Big O: O(N^2)
        # searches hashmap for address
        # once found, returns the keys associated with that address
        package = []  # in case there are multiple packages for an address
        for bucket in self.hashmap:
            for kv in bucket:
                key, items = kv
                if address in items:
                    package.append(key)
        return package
