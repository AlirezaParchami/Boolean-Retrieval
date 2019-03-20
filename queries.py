import Inverted_Index as invInd
from collections import OrderedDict
def query():
    # alireza AND friend
    t1 = "alireza"
    t2 = "friend"
    q1 = invInd.intersect(t1, t2)

    # alireza AND apologise
    t1 = "alireza"
    t2 = "apologise"
    q2 = invInd.intersect(t1, t2)

    # proud AND friend AND responsible
    t1 = "proud"
    t2 = "friend"
    t3 = "responsible"
    q3 = invInd.intersect(t1, t2, t3)

    # apologise OR mistake
    t1 = "apologise"
    t2 = "mistake"
    q4 = invInd.union(t1,t2)

    # years OR Hector OR NOT problems
    t1 = "years"
    t2 = "Hector"
    t3 = "problems"
    q5 = invInd.NOT(invInd.union(t1, t2), "OR", t3)

    # NOT apologise OR glad AND NOT meet
    t1 = "apologise"
    t2 = "glad"
    t3 = "meet"
    q6 = invInd.NOT(invInd.NOT(invInd.union(t2), "OR", t1), "AND", t3)

    # my OR best AND friend
    t1 = "my"
    t2 = "best"
    t3 = "friend"
    q7 = invInd.intersect2(invInd.union(t1,t2), t3)

    # my AND NOT his OR friend
    t1 = "my"
    t2 = "his"
    t3 = "friend"
    q8 = invInd.union2(invInd.NOT(t2, "AND", t1), t3)

    # let with me with know
    t1 = "let"
    t2 = "me"
    t3 = "know"
    q9 = invInd.with_op(t1, t2, t3)

    # please NEAR 2 know NEAR 1 it
    t1 = "please"
    t2 = "know"
    t3 = "it"
    q10 = invInd.near(2,t1,t2,1,t3)

    # twenty NEAR 2 old
    t1 = "twenty"
    t2 = "old"
    q11 = invInd.near(2, t1, t2)

    # responsible WITH for NEAR 2 problems
    t1 = "responsible"
    t2 = "for"
    t3 = "problems"
    q12 = invInd.near(0,t1,t2,2,t3)

    # twenty NEAR 1 years WITH old
    t1 = "twenty"
    t2 = "years"
    t3 = "old"
    q13 = invInd.near(1,t1,t2,0,t3)

    # let NEAR 1 know AND Hector
    t1 = "let"
    t2 = "know"
    t3 = "hector"
    q14 = invInd.intersect2(invInd.near(1,t1,t2),t3)

    # best WITH friend OR Hector
    t1 = "best"
    t2 = "friend"
    t3 = "Hector"
    q15 = invInd.union2(invInd.with_op(t1,t2),t3)

    print(q1)
    print(q2)
    print(q3)
    print(q4)
    print(q5)
    print(q6)
    print(q7)
    print(q8)
    print(q9)
    print(q10)
    print(q11)
    print(q12)
    print(q13)
    print(q14)
    print(q15)


words = invInd.words
invInd.number_of_doc = int(input("Enter Number of docs:"))
invInd.read_common_words()
invInd.read_docs()
words = OrderedDict(sorted(words.items(), key=lambda t: t[0]))
print(words)
query()