# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable_without_oops import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    table = htable(4011)
    for file_index in range(len(files)):
        s = words(get_text(files[file_index]))
        for word in s:
            if len(word)<3: #ignore words with less than 3 chars long
                continue
            else:
                table = htable_put(table, word, file_index)
            # htable_put(table, key=word, value=file_index)
    return table

def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    searched_indexes = {}
    flag = False
    temp_indexes = None
    for term in terms:
        bucket_index = hashcode(term) % len(index)
        for tpl in index[bucket_index]:
            if tpl==[]:
                continue
            elif tpl[0]==term:
                temp_indexes = tpl[1]
    
        if flag==False:
            searched_indexes = temp_indexes
            flag = True
        else:
            searched_indexes = searched_indexes.intersection(temp_indexes)
    searched_files = []
    try:
        for index_f in searched_indexes:
            searched_files.append(files[index_f])
    except:
        searched_files = []
    return searched_files   