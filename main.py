from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
frequent_words = set()
words = dict()


def read_common_words():
    f = open("frequent.txt", "r")
    for x in f:
        frequent_words.add(x.lower().rstrip('\n'))
    f.close()


def append_docId_pos(docId, indices):
    docID_pos_dic = dict()
    docID_pos_dic[docId] = indices
    return docID_pos_dic


def read_docs():
    for i in range(1, 6):
        st = str(i) + ".txt"
        my_file = open(st, "r")
        f = my_file.read().rstrip('.').rstrip(',').rstrip('?').lower()
        f = f.split()
        for word in f:
            if word not in frequent_words:  # So we will add it to our dictionary
                if word not in words:
                    indices = [i for i, x in enumerate(f) if x == word]
                    docId_pos = append_docId_pos(i, indices)
                    words[word] = docId_pos
                elif word in words:
                    print("TO DO")

        #for line in f:
        #    for word in line.split():
        #        new_word = word.rstrip('\n').rstrip('.').rstrip(',').rstrip('?').lower()
        #        if new_word not in frequent_words:  # So we will add it to out dictionary
        #            if new_word not in words:
        #                words[new_word] = i
        #                words.append(word.rstrip('\n').rstrip('.').rstrip(',').rstrip('?'))
    words.sort(key=str.lower)
    print(words)


read_common_words()
read_docs()
ps = PorterStemmer()
print(words)
for word in words:
    print(ps.stem(word))
#print(words)

