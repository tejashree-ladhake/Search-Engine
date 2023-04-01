"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    buckets =[]
    for i in range(nbuckets):
        buckets.append([])
    return buckets

def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    h = 0
    o = str(o)
    if o.isdigit()==True:
        h = int(o)
    else:
        for c in o:
            h = h*31 + ord(c)

    return h

def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """

    bucket_index = hashcode(key) % len(table)
    if len(table[bucket_index])==0:
        try:
            table[bucket_index].append((key, {value})) 
        except:
            table[bucket_index].append((key, {str(value)}))
    else:
        if key in list(map(lambda a:a[0], table[bucket_index])):
            index = [index for index in range(len(table[bucket_index])) if table[bucket_index][index][0]==key][0]
            if type(value) ==str:
                table[bucket_index][index] = (key, value)
            else:
                temp_value = table[bucket_index][index][1]
                temp_value.add(value)
                table[bucket_index][index] = (key, temp_value)
#             tpl = temp_tpl
        else:
            try:
                table[bucket_index].append((key, {value}))
            except:
                table[bucket_index].append((key, {str(value)}))

    return table


def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    # find the bucket index
    bucket_index = hashcode(key) % len(table)
    print(bucket_index)
    
    value = "None"
    for tpl in table[bucket_index]:
        if tpl[0]==key:
            value = tpl[1]
    
    return value


def htable_buckets_str(table):
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
    b_struct = ""
    for i in range(len(table)):
        flag = False
        b_struct = b_struct + '{}'.format(i).zfill(4)+'->'
        for tpl in table[i]:
            value = str([i for i in tpl[1]]).strip('[').strip(']')
#             print(value, type(value))
            if flag == False:
                b_struct = b_struct + '{}:{}'.format(tpl[0], value).replace("'","")
                flag = True
            else:
                b_struct = b_struct + ', ' + '{}:{}'.format(tpl[0], value).replace("'",'')
                
        b_struct = b_struct.rstrip(', ') +'\n'
    return b_struct

def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    b_struct = ''
    for i in range(len(table)):
        flag = False
        for tpl in table[i]:
#             print(tpl[0], [i for i in tpl[1]])
            value = str([i for i in tpl[1]]).lstrip('[').rstrip(']')
#             print(value)
            if flag == False:
                b_struct = b_struct +', ' + '{}:{}'.format(tpl[0], value).replace("'",'')
                flag = True 
            else:
                b_struct = b_struct + ', ' + '{}:{}'.format(tpl[0], value).replace("'",'')
                
    b_struct = '{' + b_struct.strip('\n').rstrip(', ').lstrip(', ') + '}'
    return b_struct