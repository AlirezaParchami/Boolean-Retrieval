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
        print(added_words)


read_common_words()
read_docs()
words = OrderedDict(sorted(words.items(), key=lambda t: t[0]))
print(words)
#ps = PorterStemmer()