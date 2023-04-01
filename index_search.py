from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    
    word_dict = defaultdict(set)
    for file_index in range(len(files)):
        s = words(get_text(files[file_index]))
        for word in s:
            if len(word)<3: #ignore words with less than 3 chars long
                continue
            else:
                word_dict[word].add(file_index)

    return word_dict

def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    word_dict = index
    searched_indexes = set()
    flag = False
    for term in terms:
        temp_indexes = word_dict[term]
        if flag==False:
            searched_indexes = temp_indexes
            flag = True
        else:
            searched_indexes = searched_indexes.intersection(temp_indexes)
    
    searched_files = []
    for index in searched_indexes:
        searched_files.append(files[index])
    return searched_files

