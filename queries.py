import Inverted_Index as invInd
from collections import OrderedDict
q = [None]*16
def query():
    # NOT friend OR Hector
    t1 = "friend"
    t2 = "Hector"
    q[0] = invInd.NOT(invInd.union(t2), "OR", t1)

    # alireza AND friend
    t1 = "alireza"
    t2 = "friend"
    q[1] = invInd.intersect(t1, t2)

    # alireza AND apologise
    t1 = "alireza"
    t2 = "apologise"
    q[2] = invInd.intersect(t1, t2)

    # proud AND friend AND responsible
    t1 = "proud"
    t2 = "friend"
    t3 = "responsible"
    q[3] = invInd.intersect(t1, t2, t3)

    # apologise OR mistake
    t1 = "apologise"
    t2 = "mistake"
    q[4] = invInd.union(t1,t2)

    # years OR Hector OR NOT problems
    t1 = "years"
    t2 = "Hector"
    t3 = "problems"
    q[5] = invInd.NOT(invInd.union(t1, t2), "OR", t3)

    # NOT apologise OR glad AND NOT meet
    t1 = "apologise"
    t2 = "glad"
    t3 = "meet"
    q[6] = invInd.NOT(invInd.NOT(invInd.union(t2), "OR", t1), "AND", t3)

    # my OR best AND friend
    t1 = "my"
    t2 = "best"
    t3 = "friend"
    q[7] = invInd.intersect2(invInd.union(t1,t2), t3)

    # my AND NOT his OR friend
    t1 = "my"
    t2 = "his"
    t3 = "friend"
    q[8] = invInd.union2(invInd.NOT(t2, "AND", t1), t3)

    # let with me with know
    t1 = "let"
    t2 = "me"
    t3 = "know"
    q[9] = invInd.with_op(t1, t2, t3)

    # please NEAR 2 know NEAR 1 it
    t1 = "please"
    t2 = "know"
    t3 = "it"
    q[10] = invInd.near(2,t1,t2,1,t3)

    # twenty NEAR 2 old
    t1 = "twenty"
    t2 = "old"
    q[11] = invInd.near(2, t1, t2)

    # responsible WITH for NEAR 2 problems
    t1 = "responsible"
    t2 = "for"
    t3 = "problems"
    q[12] = invInd.near(0,t1,t2,2,t3)

    # twenty NEAR 1 years WITH old
    t1 = "twenty"
    t2 = "years"
    t3 = "old"
    q[13] = invInd.near(1,t1,t2,0,t3)

    # let NEAR 1 know AND Hector
    t1 = "let"
    t2 = "know"
    t3 = "hector"
    q[14] = invInd.intersect2(invInd.near(1,t1,t2),t3)

    # best WITH friend OR Hector
    t1 = "best"
    t2 = "friend"
    t3 = "Hector"
    q[15] = invInd.union2(invInd.with_op(t1,t2),t3)

    for i in range(0,len(q)):
        if not q[i]:
            print("Result of query ", i, ": ", "Empty" )
        else:
            print("Result of query ", i, ": ", q[i])


words = invInd.words
invInd.number_of_doc = 5
invInd.read_common_words()
invInd.read_docs()
words = OrderedDict(sorted(words.items(), key=lambda t: t[0]))
print(words)
query()