import heapq

N = 200010
e = [0 for _ in range(N)]
ne = [0 for _ in range(N)]
h = [-1 for _ in range(N)]
w = [0 for _ in range(N)]
st = [False for _ in range(N)]
dist = [0x3f3f3f3f for _ in range(N)]

idx = 0


def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def dijstra():
    dist[1] = 0
    l = []
    heapq.heapify(l)
    heapq.heappush(l, (0, 1))
    while l:
        t = heapq.heappop(l)
        distance = t[0]
        ver = t[1]
        if st[ver]:
            continue
        st[ver] = True

        i = h[ver]
        while i != -1:
            j = e[i]
            if dist[j] > distance + w[i]:
                dist[j] = distance + w[i]
                heapq.heappush(l, (dist[j], j))
            i = ne[i]


n, m = map(int, input().split())

for _ in range(m):
    a, b, c = map(int, input().split())
    add(a, b, c)
    add(b, a, c)
dijstra()
res = 0

for a in range(2, n + 1):
    minw = float('inf')
    j = h[a]
    while j != -1:
        b = e[j]
        if dist[a] == dist[b] + w[j]:
            minw = min(minw, w[j])
        j = ne[j]
    res += minw
print(res)




