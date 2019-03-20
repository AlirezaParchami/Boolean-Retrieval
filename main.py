from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import OrderedDict
frequent_words = set()
words = dict()
ps = PorterStemmer()

def read_common_words():
    f = open("frequent.txt", "r")
    for x in f:
        frequent_words.add(x.lower().rstrip('\n'))
    f.close()


def append_docId_pos(docId, indices, docID_pos_dic):
    if docId not in docID_pos_dic.keys():
        docID_pos_dic[docId] = indices
    elif docId in docID_pos_dic.keys():
        positions = docID_pos_dic[docId]
        positions = positions + indices
        docID_pos_dic[docId] = positions
    return docID_pos_dic


def read_docs():
    for i in range(1, 6):
        st = str(i) + ".txt"
        my_file = open(st, "r")
        f = my_file.read().lower()
        f = f.split()
        # We find all indices of a word in document and add in Inverted index
        # So I add the word in added_words[] to prevent appear repeated indices for same docID in inverted list.
        added_words = []
        for word in f:
            # I should consider the main part of word
            edited_word = word.replace('.', '').replace('?', '').replace(',', '')
            stem_word = ps.stem(edited_word)
            # I use edited_word in condition because stem_word is wrong.
            # Ex. friends and friend are different words that I should find its indices but have same stem
            if stem_word not in frequent_words and edited_word not in added_words:
                # I should find original from of word through document
                indices = [i for i, x in enumerate(f) if x == word]
                if stem_word not in words.keys():
                    # Entry_value is a dictionary of docID and Positions
                    entry_value = append_docId_pos(i, indices, dict())
                    words[stem_word] = entry_value
                    added_words.append(edited_word)
                elif stem_word in words.keys():
                    entry_value = dict(words.get(stem_word))
                    entry_value = append_docId_pos(i, indices, entry_value)
                    words[stem_word] = entry_value
                    added_words.append(edited_word)


def read_queries(num):
    for i in range(1, num):
        st = "./Queries/" + str(i) + ".txt"
        my_file = open(st, "r")
        f = my_file.read()
        f = f.split()
        keywords = [i for i, x in enumerate(f) if x == 'AND' or x == 'OR' or x == 'NOT' or x == 'with' or x == 'Near']
        print(keywords)
        result = []

        for j in range(0, len(keywords)-1):
            if (keywords[j+1] == keywords[j] + 1) and (f[keywords[j]] == "OR" or f[keywords[j]] == "AND") and (f[keywords[j+1]] != "NOT"):
                result = "invalid"
                break
        if result == "invalid":
            print("Invalid Query!")
            continue

        for index in keywords:
            if f[index] == "AND":
                left_operand = f[index-1]
                not_operand = False
                right_operand = f[index+1]
                if index + 1 in keywords:  # The word must be "NOT"
                    not_operand = True
                    right_operand = f[index+2]


def intersect(t1, t2):
    global words
    t1 = ps.stem(t1)
    t2 = ps.stem(t2)
    doc1 = set(words[t1].keys())
    doc2 = set(words[t2].keys())
    result = doc1.intersection(doc2)
    print(result)
    return result

def union(t1, t2):
    global words
    t1 = ps.stem(t1)
    t2 = ps.stem(t2)
    doc1 = set(words[t1].keys())
    doc2 = set(words[t2].keys())
    result = doc1.union(doc2)
    print(result)
    return result

def NOT(t1):
    global words
    t1 = ps.stem(t1)
    doc1 = set(words[t1].keys())
    print(doc1)
    result = set(range(1, 7)).difference(doc1)
    print(result)
    return result


read_common_words()
read_docs()
words = OrderedDict(sorted(words.items(), key=lambda t: t[0]))
print(words)
print((list(words.values())))
#query_numbers = 7
#print(query_numbers)
#read_queries(query_numbers)
t1 = "alireza"
t2 = "computer"
#intersect(t1, t2)
#union(t1,t2)
NOT(t2)