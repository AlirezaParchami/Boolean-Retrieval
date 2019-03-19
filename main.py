#from nltk.stem import PorterStemmer
#from nltk.tokenize import sent_tokenize, word_tokenize
from collections import OrderedDict
frequent_words = set()
words = dict()


def read_common_words():
    f = open("frequent.txt", "r")
    for x in f:
        frequent_words.add(x.lower().rstrip('\n'))
    f.close()


def append_docId_pos(docId, indices, docID_pos_dic):
#    docID_pos_dic = dict()
    docID_pos_dic[docId] = indices
    return docID_pos_dic


def read_docs():
    for i in range(1, 6):
        st = str(i) + ".txt"
        my_file = open(st, "r")
        f = my_file.read().lower()
        f = f.split()
        for word in f:
            edited_word = word.replace('.', '').replace('?', '').replace(',', '')
            if edited_word not in frequent_words:  # So we will add it to our dictionary
                indices = [i for i, x in enumerate(f) if x == word]
                if edited_word not in words:
                    entry_value = append_docId_pos(i, indices, dict())  # Entry_value is a dictionary of docID and Positions
                    words[edited_word] = entry_value
                elif edited_word in words:
                    entry_value = dict(words.get(edited_word))
                    entry_value = append_docId_pos(i, indices, entry_value)
                    words[edited_word] = entry_value

        #for line in f:
        #    for word in line.split():
        #        new_word = word.rstrip('\n').rstrip('.').rstrip(',').rstrip('?').lower()
        #        if new_word not in frequent_words:  # So we will add it to out dictionary
        #            if new_word not in words:
        #                words[new_word] = i
        #                words.append(word.rstrip('\n').rstrip('.').rstrip(',').rstrip('?'))
    #sorted(words.keys(), key= lambda x:x[0])
    #print(words)


read_common_words()
read_docs()
words = sorted(words.items(), key=lambda t: t[0])
#ps = PorterStemmer()
print(words)