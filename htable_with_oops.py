"""
A HashTable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

class HashTable:
    def __init__(self, nbuckets):
        """Init with a list of nbuckets lists"""
        self.table = [[] for i in range(nbuckets)]
        self.buckets = nbuckets


    def __len__(self):
        """
        number of keys in the hashable
        """
        count = 0
        for item in self.table:
            if item == []:
                continue
            else:
                count += len(item)
        return count



    def __setitem__(self, key, value):
        """
        Perform the equivalent of table[key] = value
        Find the appropriate bucket indicated by key and then append (key,value)
        to that bucket if the (key,value) pair doesn't exist yet in that bucket.
        If the bucket for key already has a (key,value) pair with that key,
        then replace the tuple with the new (key,value).
        Make sure that you are only adding (key,value) associations to the buckets.
        The type(value) can be anything. Could be a set, list, number, string, anything!
        """
        # h = hash(key) % len(self.buckets)
        h = hash(key) % self.buckets
        keyss = self.keys()
        if (key in keyss):
            for j, d in enumerate(self.table[h]):
                if d[0]==key:
                    self.table[h][j] = (key, value)
        else:
            self.table[h].append((key, value))


    def __getitem__(self, key):
        """
        Return the equivalent of table[key].
        Find the appropriate bucket indicated by the key and look for the
        association with the key. Return the value (not the key and not
        the association!). Return None if key not found.
        """
        # h = hash(key) % len(self.buckets)
        h = hash(key) % self.buckets
        
        if key not in self.keys():
            return None
        for item in self.table[h]:
            if item[0] == key:
                return item[1]


    def __contains__(self, key):
        flag = False
        # bucket_index = hash(key) % self.buckets
        # if bucket_index in range(self.buckets):
        #     for item in self.table:
        #         if item[0] == key:
        #             flag = True
        keyss = self.keys()
        if key in keyss:
            return True
        else:
            return False    
        # return flag
        

    def __iter__(self):
        return (j[0] for k in self.table for j in k if k!=[])


    def keys(self):
        """
        return all keys in the hashtable

        Returns
        -------
        elems : TYPE
            DESCRIPTION.

        """
        keys = []
        for items in self.table:
            if items == []:
                continue
            else:
                for j in items:
                    keys.append(j[0])
        return keys


    def items(self):
        """
        returns all values in the hashable

        """
        lst = []
        for item in self.table:
            if item == []:
                continue
            for j in item:
                lst.append(j)
        return lst

        
    def __repr__(self):
        """
        Return a string representing the various buckets of this table.
        The output looks like:
            0000->
            0001->
            0002->
            0003->parrt:99
            0004->
        where parrt:99 indicates an association of (parrt,99) in bucket 3.
        """
        str1=''
        list2=[]

        for i in range(len(self.table)):
            for j, d in enumerate(self.table[i]):
                list2.append(f"{d[0]}:{d[1]}")

        return '{'+", ".join(list2)+'}'


    def __str__(self):
        """
        Return what str(table) would return for a regular Python dict
        such as {parrt:99}. The order should be in bucket order and then
        insertion order within each bucket. The insertion order is
        guaranteed when you append to the buckets in htable_put().
        """
        list2=[]

        for i in range(len(self.table)):
            for j, d in enumerate(self.table[i]):
                if d != []:
                    list2.append(f"{d[0]}:{d[1]}")

        return '{'+", ".join(list2)+'}'



    def bucket_indexof(self, key):
        """
        You don't have to implement this, but I found it to be a handy function.

        Return the index of the element within a specific bucket; the bucket is:
        table[hashcode(key) % len(table)]. You have to linearly
        search the bucket to find the tuple containing key.
        """
        # h = hash(key) % len(self.buckets)
        
