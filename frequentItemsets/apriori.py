import json
import re

threshold = 2

def apriori(L):
    print(L)
    L = list(L)
    C = set([])
    for a in L:
        for b in L:
            if a > b:
                if len(set(a) | set(b)) == len(a) + 1:
                    C.add(tuple(set(a) | set(b)))
    print(C)
    C_del = set([])
    for itemsets in C:
        prune = False
        itemsetsList = list(itemsets)
        for i in range(len(itemsetsList)):
            #print(tuple(itemsetsList[:i] + itemsetsList[i+1:]))
            if tuple(itemsetsList[:i] + itemsetsList[i+1:]) not in L:
                prune = True
                break
        if prune:
            C_del.add(itemsets)
    for itemsets in C_del:
        C.remove(itemsets)
    print(C)
    return C


def init(T):
    global threshold
    itemsets = []
    for Ti in T:
        for item in Ti:
            itemsets.append(item)
    itemsets.sort()
    cnt = 1
    L = set([])
    for i in range(len(itemsets)):
        if i == 0:
            continue
        if itemsets[i] != itemsets[i-1]:
            if cnt >= threshold:
                L.add(tuple(itemsets[i-1],))
            cnt = 1
        else:
            cnt += 1
    if cnt >= threshold:
        L.add(tuple(itemsets[-1]))
    return L

T = []
p = re.compile(r'\'[0-9]*\'')
with open('data.txt','r') as fin:
    for line in fin.readlines():
        items = line.strip().split(',')
        T.append(items)

L = []
L.append(init(T))

while True:
    nL = apriori(L[-1])
    if len(nL) == 0:
        break
    L.append(nL)
print(L)




