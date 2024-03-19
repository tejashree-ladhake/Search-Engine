# Search Engine Implementation


# Overview

The project involves implementing three different search mechanisms: a linear search, a hashtable search using Python’s built-in **`dict`** objects, and a hashtable search using a custom implementation. All three mechanisms should give the same results, but the linear search is expected to be much slower.

The project also includes creating an index for faster lookups and generating HTML output to display the search results. The data sets used for the project are articles from Slate magazine and Berlitz travelogues.

# Dataset

A search engine takes in one or more search terms and looks for files within a corpus that contain all of those terms. A corpus is a collection of text files, often organized within a directory and its subdirectories. For example, the American National corpus contains a large amount of text data. In this project, articles from **Slate magazine** and **Berlitz travelogues** have been extracted for use as data sets. 

![Screen Shot 2023-04-01 at 4.52.31 PM.png](Search%20Engine%20Implementation%206e9e9f0f7f564199b65b1e2c27a0d410/Screen_Shot_2023-04-01_at_4.52.31_PM.png)

# Methodologies:

## Linear Search:

The first step in this project is to implement a linear search algorithm that checks each file to see if it contains all the search terms. Matching filenames are added to a list. The time complexity is O(kn), where k is the average number of words per file and n is the number of files, but it can be approximated as O(n).

## Hash Table using dict():

Instead of searching each file for every query, creating an index that maps words to the files containing them is more efficient. The search results for multiple words are found by computing each word's intersection of the document sets. The index returns a set or unique list of document indexes, avoiding duplication of filename strings

![Screen Shot 2023-04-01 at 4.53.22 PM.png](Search%20Engine%20Implementation%206e9e9f0f7f564199b65b1e2c27a0d410/Screen_Shot_2023-04-01_at_4.53.22_PM.png)

Received message. Instead of searching each file for every query, creating an index that maps words to the files containing them is more efficient. The search results for multiple words are found by computing each word's intersection of the document sets. The index returns a set or unique list of document indexes, avoiding duplication of filename strings.

Creating an index takes about the same time as performing one linear search because both involve going through the list of files. The complexity of index creation is O(n) for n total words in all files. However, once the index is created, searching takes constant time, or O(1).

## Index Search using a custom Hash Table:

### Computing hash codes:

Hash codes are computed for string and integer keys **supports any object as key, not just strings and integers** and the mapped values can be of any type. The hash code for a string could be the sum of its character ASCII codes, but this could result in many collisions. A collision occurs when different keys hash to the same bucket. The distribution of elements to buckets depends on the number of buckets and the quality of the hash function. 

I used the built-in `hash(o)` function to get hashcodes for all key objects:

```python
h = hash(key) % len(self.buckets)
```

**Object-oriented implementation of the hash table:**

```python
class HashTable:
    def __init__(self, nbuckets):
        """Init with a list of nbuckets lists"""
        self.table = [[] for i in range(nbuckets)]
        self.buckets = nbuckets
```

A HashTable represented as a list of lists with open hashing.
Each bucket is a list of (key, value) tuples

![Screen Shot 2023-04-01 at 4.58.04 PM.png](Search%20Engine%20Implementation%206e9e9f0f7f564199b65b1e2c27a0d410/Screen_Shot_2023-04-01_at_4.58.04_PM.png)

I implemented `__get__`and `__set__`functions to perform the equivalent function of get table[key] and setting the value in the table for table[key] = value

```python
def __getitem__(self, key):
        h = hash(key) % self.buckets
        if key not in self.keys():
            return None
        for item in self.table[h]:
            if item[0] == key:
                return item[1]
```

This function returns the equivalent of table[key]. And find the appropriate bucket indicated by the key and look for the association with the key. And return the value (not the key or
the association!). Return None if key not found.

```python
def __setitem__(self, key, value):
        h = hash(key) % self.buckets
        keyss = self.keys()
        if (key in keyss):
            for j, d in enumerate(self.table[h]):
                if d[0]==key:
                    self.table[h][j] = (key, value)
        else:
            self.table[h].append((key, value))
```

 This function Performs the equivalent of table[key] = value where it finds the appropriate bucket indicated by the key and then appends (key, value) to that bucket if the (key, value) pair doesn't exist yet in that bucket. If the bucket for the key already has a (key, value) pair with that key, then replace the tuple with the new (key, value). Make sure that you are only adding (key, value) associations to the buckets. The type(value) can be anything. It could be a set, list, number, string, or anything!

![Screen Shot 2023-04-01 at 2.35.55 PM.png](Search%20Engine%20Implementation%206e9e9f0f7f564199b65b1e2c27a0d410/Screen_Shot_2023-04-01_at_2.35.55_PM.png)

In our case our values for the association are sets of document IDs. If `ronald` is in documents 9 and 3 and `reagan` is in document 17 and both of those terms hashed to bucket 0, you would see the following 2-element bucket 0 with two associations:

# Results:

I have used the template engine [jinja2](http://jinja.pocoo.org/docs/2.9/), part of the flask web server, to create the HTML.

![Untitled](Search%20Engine%20Implementation%206e9e9f0f7f564199b65b1e2c27a0d410/Untitled.png)

For visualization of table structure, I have used **`from** lolviz **import**``objviz`
