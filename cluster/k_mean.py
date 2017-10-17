import random

global point
global k

def minloc(a):
    return a.index(min(a))

def k_mean(belong):
    global point
    global k

    rep = [(0,0) for i in range(k)]
    num = [0 for i in range(k)]

    #计算中心
    for i in range(len(point)):
        (x,y) = rep[belong[i]]
        rep[belong[i]] = (x + point[i][0], y + point[i][1])
        num[belong[i]] += 1


    for i in range(k):
        (x,y) = rep[i]
        rep[i] = (x/num[i],y/num[i])

    nbel = []
    #计算归属
    for (x,y) in point:
        dis = [((x-x0)*(x-x0)+(y-y0)*(y-y0)) for (x0,y0) in rep]
        nbel.append(minloc(dis))

    return nbel







#对象集
minx = 0
maxx = 20
miny = 0
maxy = 20

n = 10

point = [(random.uniform(minx,maxx),random.uniform(miny,maxy)) for i in range(n)]
print(point)

#聚类数
k = 3

#初始中心
p = [x for x in range(n)]
random.shuffle(p)
rep = [point[p[x]] for x in range(k)]

#点归属
belong = []
for (x,y) in point:
    dis = [((x-x0)*(x-x0)+(y-y0)*(y-y0)) for (x0,y0) in rep]
    belong.append(minloc(dis))

print(belong)
#k_means迭代
cnt = 0
iter_limit = 100

while True:
    nbel = k_mean(belong)
    if nbel == belong:
        break
    else:
        belong = nbel

    print(belong)

    cnt += 1
    if cnt >= iter_limit:
        break

print(belong)
