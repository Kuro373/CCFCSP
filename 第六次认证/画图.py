#画布的左下角是坐标为 (0,0)的位置，向右为 x坐标增大的方向，向上为 y 坐标增大的方向。
#以前做题的时候都是左上角为(0,0)，而左下角为(0,0)的情况可以视作在最后输出的时候左上角逆序
#在可以dfs和bfs的情况下一定要选bfs,因为dfs容易爆
N = 110
from collections import deque
g = [['.' for _ in range(N)] for _ in range(N)]
st = [[False for _ in range(N)] for _ in range(N)]


def change(x1, y1, x2, y2):
    if x1 == x2:
        for i in range(y1, y2 + 1):
            if g[x1][i] in "|+":
                g[x1][i] = "+"
            else:
                g[x1][i] = "-"
    elif y1 == y2:
        for i in range(x1, x2 + 1):
            if g[i][y1] in "+-":
                g[i][y1] = "+"
            else:
                g[i][y1] = "|"


def paint(x, y, s):
    st[x][y] = True
    g[x][y] = s
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque([(x, y)])
    while q:

        t = q.popleft()
        x, y = t[0], t[1]
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if a < 0 or b < 0 or a >= n or b >= m or g[a][b] in "|-+" or st[a][b]:
                continue
            g[a][b] = s
            q.append((a, b))
            st[a][b]=True


m, n, q = map(int, input().split())

for _ in range(q):
    # for i in range(n - 1, -1, -1):
    #     print(*g[i][:m])
    l = list(input().split())
    if l[0] == "0":
        y1, x1, y2, x2 = map(int, l[1:])
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        change(x1, y1, x2, y2)
    else:

        y, x, s = int(l[1]), int(l[2]), l[3]
        #print(x,y)
        st = [[False for _ in range(N)] for _ in range(N)]
        paint(x, y, s)
for i in range(n - 1, -1, -1):
    print("".join(g[i][:m]))
# for i in range(5):
#     print(*g[i])