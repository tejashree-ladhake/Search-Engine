import os
import re
import string


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    path = root
    files = []
    dirs = os.listdir(root)
    if os.path.isdir(path+'/'+dirs[0])==True:
        for i in dirs:
            try:
                file_names = os.listdir(path+'/'+i)
                for file in file_names:
                    files.append(path+'/'+ i+ '/'+file)
            except:
                continue
    else:
        file_names = os.listdir(path)
        for file in file_names:
            files.append(path+'/'+file)
    return files

def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):    
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    terms_combined =''
    for t in terms:
        terms_combined = terms_combined + t +' '
    terms_combined = terms_combined.rstrip(' ')
    terms.append(terms_combined)
    
    output = dict() #{file_name: string with keywords upto 3 searches}
    for file in docs:
        loc_lst = []
        countt = 1 
        s = get_text(file).lower()
        # clean the file content with spaces and \n
        s = s.replace('\n',' ')
        s = s.replace('\'','')
        s = " ".join(s.split())
        
        # find the loc of the searched words:
        
        for term in terms[-1::-1]: # check if the combination of words exists
            if term == terms[-1]:
                if s.find(term)!=-1:
                    loc_lst.append(s.find(term))
                    break
                else:
                    continue

            else:
                loc_lst.append(s.find(term))
#         print(loc_lst)
                

        for loc in loc_lst:
            if countt<3: # print the 3 searches only
                if (loc-40<0) or (loc+40)>len(s):
                    txt_lst =s[:81].split(' ')
                else:
                    txt_lst =s[loc-40: loc+40].split(' ') # drop first and last element - they can be incomplete words
                if file in output.keys():
                    output[file].append(" ".join(txt_lst[1:-1]))
                else:
                    output[file] = [" ".join(txt_lst[1:-1])]
                countt = countt+1
#     print(output)
        with open('output.txt', 'w') as f:
            f.write(str(output))
          
    terms_template = ''
    for t in terms:
        terms_template = terms_template+t+ ' '
    terms_template = terms_template.rstrip(' ')

    html_template = '<html>\n    <body>\n    <h2>Search results for <b>{}</b> in {} files</h2>'.format(terms[-1], len(output))
    count = 1
    for file, search in output.items():
        if count <= 100:
            string = ''
            for s in search:
                string = string + s + '<br>'

            for t in terms:
                l = string.find(t)
                string = string.replace(t, '<b>{}</b>'.format(t))
            count = count+1
        else:
            break
            
        html_template = html_template + '\n\n        <p><a href="{}">{}</a><br>\n        {}<br><br>\n'.format(file, file, string)
    html_template = html_template +'\n</body>\n</html>'
    return html_template  
      

def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]
