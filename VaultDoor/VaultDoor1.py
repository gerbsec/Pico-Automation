

with open('indexes', 'r') as index:
    index = index.read().split()

with open('yes', 'r') as let:
    let = let.read().split()
index = [int(item) for item in index]
yes = zip(let , index)
def Sort_Tuple(tup):
     
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
         
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup

for i in Sort_Tuple(list(yes)):
    print(i[0], end='')
