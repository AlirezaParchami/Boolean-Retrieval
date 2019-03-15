f = open("frequent.txt" , "r")
frequent = set()
for x in f:
    frequent.add(x.lower().rstrip('\n'))
f.close()

words = list()
for i in range(1,6):
    st = str(i) + ".txt"
    f = open(st,"r")
    for line in f:
        for word in line.split():
            if word.lower() not in frequent:
               words.append(word.rstrip('\n').rstrip('.').rstrip(',').rstrip('?'))

words.sort(key=str.lower)
print(words)