#bfs暴力:60分
from collections import deque
N=1010
M=100010
e=[0 for _ in range(M)]
ne=[0 for _ in range(M)]
h=[-1 for _ in range(N)]

idx=0
def add(a,b):
    global idx
    e[idx]=b
    ne[idx]=h[a]

    h[a]=idx
    idx+=1
g=[[False for _ in range(N)] for _ in range(N)]

def bfs():
    global q
    while q:
        t=q.popleft()
        a,b=t[0],t[1]
        j=h[b]
        while j!=-1:
            if g[a][e[j]]:
                j=ne[j]
                continue
            q.append([a,e[j]])
            g[a][e[j]]=True
            j=ne[j]
q=deque()
n,m=map(int,input().split())
for i in range(m):
    a,b=map(int,input().split())
    add(a,b)
    q.append([a,b])

bfs()
res=0
for i in range(1,n+1):
    for j in range(1,i):
        if g[i][j] and g[j][i]:
            res+=1

print(res)
