import main as m
def query():
    t1 = ""
    t2 = ""
    t3 = ""

    # alireza AND friend
    t1 = "alireza"
    t2 = "friend"
    q1 = m.intersect(t1, t2)

    # alireza AND apologise
    t1 = "alireza"
    t2 = "apologise"
    q2 = m.intersect(t1, t2)

    # proud AND friend AND responsible
    t1 = "proud"
    t2 = "friend"
    t3 = "responsible"
    q3 = m.intersect(t1, t2, t3)

    # apologise OR mistake
    t1 = "apologise"
    t2 = "mistake"
    q4 = m.union(t1,t2)

    # years OR Hector OR NOT problems
    t1 = "years"
    t2 = "Hector"
    t3 = "problems"
    q5 = m.NOT(m.union(t1, t2), "OR", t3)

    # NOT apologise OR glad AND NOT meet
    t1 = "apologise"
    t2 = "glad"
    t3 = "meet"
    q6 = m.NOT(m.NOT(m.union(t2), "OR", t1), "AND", t3)

    # my OR best AND friend
    t1 = "my"
    t2 = "best"
    t3 = "friend"
    q7 = m.intersect2(m.union(t1,t2), t3)

    # my AND NOT his OR friend
    t1 = "my"
    t2 = "his"
    t3 = "friend"
    q8 = m.union2(m.NOT(t2, "AND", t1), t3)

    # let with me with know
    t1 = "let"
    t2 = "me"
    t3 = "know"
    q9 = m.with_op(t1, t2, t3)

    # please NEAR 2 know NEAR 1 it
    t1 = "please"
    t2 = "know"
    t3 = "it"
    q10 = m.near(2,t1,t2,1,t3)

    # twenty NEAR 2 old
    t1 = "twenty"
    t2 = "old"
    q11 = m.near(2, t1, t2)