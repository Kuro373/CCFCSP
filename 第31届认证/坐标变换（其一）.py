'''
Acwing原题链接:
https://www.acwing.com/problem/content/5300/
'''
n,m=map(int,input().split())

dx,dy=0,0
for i in range(n):
    a,b=map(int,input().split())
    dx+=a
    dy+=b
for i in range(m):
    x,y=map(int,input().split())
    print(x+dx,y+dy)