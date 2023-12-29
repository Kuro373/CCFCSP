
'''
已经是屎山代码了，只差输入的路径最开始是根目录的情况
例如'/../././///'
之类的
'''

n=int(input())
curs=input()
cur=[]
tmp=""
for i in curs:

    if i=="/":
        if not tmp:
            continue
        cur.append(tmp)
        tmp=""
    else:
        tmp=tmp+i
if tmp:
    cur.append(tmp)
for _ in range(n):
    tmpcur=cur.copy()
    ops= input()
    op = []
    tmp = ""
    for i in ops:
        if i == "/":
            if not tmp:
                continue
            op.append(tmp)
            tmp=""
        else:
            tmp = tmp + i
    if tmp:
        op.append(tmp)
    #print(f"op:{op}")
    if not ops:
        for i in cur:
            print("/",end="")
            print(i,end="")
        print()
    elif not op:
        print("/")
    elif '.' not in op and '..' not in op:
        for i in op:
            print("/",end="")
            print(i,end="")
        print()

    else:

        if op[0] == "..":
            if ops[0]!='/':
                op.pop(0)
                op = tmpcur[:-1] + op
            else:
                op.pop(0)
        elif op[0] == ".":
           if ops[0]!='/':
                op.pop(0)
                op = tmpcur + op
           else:
               op.pop(0)
        tmpop = op.copy()


        if op:
            for i in range(len(op)):
                if op[i]=="..":
                    tmpop[i]=""
                    for j in range(i-1,-1,-1):
                        if tmpop[j]:
                            tmpop[j]=''
                            break

                elif op[i]==".":
                    tmpop[i]=""

        #print(f"tmp:{tmpop}")
        flag=False
        for i in tmpop:
            if i:
                flag=True
        if flag:
            for i in tmpop:
                if i:
                    print("/",end="")
                    print(i,end="")
        else:
            print('/',end="")
        print()


