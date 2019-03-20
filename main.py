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
    global number_of_doc
    for i in range(1, number_of_doc + 1):
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


def intersect(t1, t2=None, t3=None):
    global words
    t1 = ps.stem(t1)
    doc1 = set(words[t1].keys())
    if t2==None:
        return doc1
    t2 = ps.stem(t2)
    doc2 = set(words[t2].keys())
    if t3==None:
        result = doc1.intersection(doc2)
    else:
        t3 = ps.stem(t3)
        doc3 = set(words[t3].keys())
        result = doc1.intersection(doc2).intersection(doc3)
    return result


def union(t1, t2=None, t3=None):
    global words
    t1 = ps.stem(t1)
    doc1 = set(words[t1].keys())
    if t2==None:
        return doc1
    t2 = ps.stem(t2)
    doc2 = set(words[t2].keys())
    if t3==None:
        result = doc1.union(doc2)
    else:
        t3 = ps.stem(t3)
        doc3 = set(words[t3].keys())
        result = doc1.union(doc2).union(doc3)
    return result


def NOT(t1 , op, t2):
    global words
    t1 = set(t1)
    t2 = ps.stem(t2)
    doc1 = set(words[t2].keys())
    result_t2 = set(range(1, number_of_doc+1)).difference(doc1)
    if op == "AND":
        result = t1 & result_t2
    elif op == "OR":
        result = t1 | result_t2
    else:
        "The Operand has not defined."
        result = 0
    return result


def with_op(t1, t2, t3=None):
    global words
    result = []
    t1 = ps.stem(t1)
    t2 = ps.stem(t2)
    doc1 = OrderedDict(words[t1])
    doc2 = OrderedDict(words[t2])
    if t3 == None:
        for x in set(doc2.keys()).intersection(set(doc1.keys())):
            d1 = doc1[x]
            d2 = doc2[x]
            for index in d1:
                if index+1 in d2:
                    result.append(x)
                    break
    else:
        t3 = ps.stem(t3)
        doc3 = OrderedDict(words[t3])
        for x in set(set(doc2.keys()).intersection(set(doc1.keys()))).intersection(set(doc3.keys())):
            d1 = doc1[x]
            d2 = doc2[x]
            d3 = doc3[x]
            for index in d1:
                if index + 1 in d2 and index + 2 in d3:
                    result.append(x)
                    break
    return result


def near(num, t1, t2, num2=None, t3=None):
    global words
    result = []
    t1 = ps.stem(t1)
    t2 = ps.stem(t2)
    doc1 = OrderedDict(words[t1])
    doc2 = OrderedDict(words[t2])
    if num2==None and t3==None:
        for x in set(doc2.keys()).intersection(set(doc1.keys())):
            d1 = doc1[x]
            d2 = doc2[x]
            for index in d1:
                for index2 in d2:
                    if 1 <= index2 - index <= num +1:
                        result.append(x)
                        break
        return result
    else:
        t3 = ps.stem(t3)
        doc3 = OrderedDict(words[t3])
        for x in set(set(doc2.keys()).intersection(set(doc1.keys()))).intersection(set(doc3.keys())):
            d1 = doc1[x]
            d2 = doc2[x]
            d3 = doc3[x]
            maybe_true = False
            for index in d1:
                for index2 in d2:
                    if 1 <= index2 - index <= num + 1 :
                        maybe_true = True
                        break
                if maybe_true == True:
                    break
            for index2 in d2:
                for index3 in d3:
                    if 1 <= index3 - index2 <= num2 + 1:
                        if maybe_true == True:
                            result.append(x)
                            return result


def intersect2(t1, t2):
    global words
    t2 = ps.stem(t2)
    doc2 = set(words[t2].keys())
    t1 = set(t1)
    return t1 & doc2


def union2(t1,t2):
    global words
    t2 = ps.stem(t2)
    doc2 = set(words[t2].keys())
    t1 = set(t1)
    return t1 | doc2


def query():
    # alireza AND friend
    t1 = "alireza"
    t2 = "friend"
    q1 = intersect(t1, t2)

    # alireza AND apologise
    t1 = "alireza"
    t2 = "apologise"
    q2 = intersect(t1, t2)

    # proud AND friend AND responsible
    t1 = "proud"
    t2 = "friend"
    t3 = "responsible"
    q3 = intersect(t1, t2, t3)

    # apologise OR mistake
    t1 = "apologise"
    t2 = "mistake"
    q4 = union(t1,t2)

    # years OR Hector OR NOT problems
    t1 = "years"
    t2 = "Hector"
    t3 = "problems"
    q5 = NOT(union(t1, t2), "OR", t3)

    # NOT apologise OR glad AND NOT meet
    t1 = "apologise"
    t2 = "glad"
    t3 = "meet"
    q6 = NOT(NOT(union(t2), "OR", t1), "AND", t3)

    # my OR best AND friend
    t1 = "my"
    t2 = "best"
    t3 = "friend"
    q7 = intersect2(union(t1,t2), t3)

    # my AND NOT his OR friend
    t1 = "my"
    t2 = "his"
    t3 = "friend"
    q8 = union2(NOT(t2, "AND", t1), t3)

    # let with me with know
    t1 = "let"
    t2 = "me"
    t3 = "know"
    q9 = with_op(t1, t2, t3)

    # please NEAR 2 know NEAR 1 it
    t1 = "please"
    t2 = "know"
    t3 = "it"
    q10 = near(2,t1,t2,1,t3)

    # twenty NEAR 2 old
    t1 = "twenty"
    t2 = "old"
    q11 = near(2, t1, t2)

    # responsible WITH for NEAR 2 problems
    t1 = "responsible"
    t2 = "for"
    t3 = "problems"
    q12 = near(0,t1,t2,2,t3)

    # twenty NEAR 1 years with old
    t1 = "twenty"
    t2 = "years"
    t3 = "old"
    q13 =  near(1,t1,t2,0,t3)



number_of_doc = int(input("Enter Number of docs:"))
read_common_words()
read_docs()
words = OrderedDict(sorted(words.items(), key=lambda t: t[0]))
print(words)
# query_numbers = 7
# print(query_numbers)
# read_queries(query_numbers)
# intersect(t1, t2)
# union(t1,t2)
# NOT(t2)
# with_op(t1, t2, t3)
#print(near(1,t1,t3))
query()
