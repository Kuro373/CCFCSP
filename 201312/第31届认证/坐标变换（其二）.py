'''
Acwing 原题链接：
https://www.acwing.com/problem/content/5301/
'''
from math import cos,sin
n,m=map(int,input().split())
op=[]

for i in range(n):
    a,b=map(float,input().split())
    op.append([a,b])
s=[[1,0] for _ in range(len(op)+1)]

#前缀和操作
for i in range(1,1+len(op)):
    #拉伸
    if int(op[i-1][0])==1:
        s[i][0]=op[i-1][1]*s[i-1][0]
        s[i][1]=s[i-1][1]
    #theta
    else:
        s[i][0]=s[i-1][0]
        s[i][1]=op[i-1][1]+s[i-1][1]
#print(s)

for _ in range(m):

    i,j,x,y=map(int,input().split())
    x*=(s[j][0]/s[i-1][0])
    y*=(s[j][0]/s[i-1][0])
    t=s[j][1]-s[i-1][1]
   #易知旋转后的横坐标为 xcosθ−ysinθ纵坐标为 xsinθ+ycosθ
    #print(x,y)
    print(x*cos(t)-y*sin(t),x*sin(t)+y*cos(t))

