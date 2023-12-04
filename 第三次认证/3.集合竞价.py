'''
问题描述
　　某股票交易所请你编写一个程序，根据开盘前客户提交的订单来确定某特定股票的开盘价和开盘成交量。
　　该程序的输入由很多行构成，每一行为一条记录，记录可能有以下几种：
　　1. buy p s 表示一个购买股票的买单，每手出价为p，购买股数为s。
　　2. sell p s 表示一个出售股票的卖单，每手出价为p，出售股数为s。
　　3. cancel i表示撤销第i行的记录。
　　如果开盘价为p0，则系统可以将所有出价至少为p0的买单和所有出价至多为p0的卖单进行匹配。因此，此时的开盘成交量为出价至少为p0的买单的总股数和所有出价至多为p0的卖单的总股数之间的较小值。
　　你的程序需要确定一个开盘价，使得开盘成交量尽可能地大。如果有多个符合条件的开盘价，你的程序应当输出最高的那一个。
输入格式
　　输入数据有任意多行，每一行是一条记录。保证输入合法。股数为不超过108的正整数，出价为精确到恰好小数点后两位的正实数，且不超过10000.00。
输出格式
　　你需要输出一行，包含两个数，以一个空格分隔。第一个数是开盘价，第二个是此开盘价下的成交量。开盘价需要精确到小数点后恰好两位。
样例输入
buy 9.25 100
buy 8.88 175
sell 9.00 1000
buy 9.00 400
sell 8.92 400
cancel 1
buy 100.00 50
样例输出
9.00 450
评测用例规模与约定
　　对于100%的数据，输入的行数不超过5000。
'''


'''
最重要的话：
如果开盘价为 p0
，则系统可以将所有出价至少为 p0
 的买单和所有出价至多为 p0
 的卖单进行匹配。

因此，此时的开盘成交量为出价至少为 p0
 的买单的总股数和所有出价至多为 p0
 的卖单的总股数之间的较小值。'''

N = 5010

st = [False for _ in range(N)]
records = [None for _ in range(N)]

cnt = 0

while True:
    try:
        cnt += 1
        op, *nums = input().split()
        if op == "cancel":
            st[int(nums[0])] = False
        else:
            st[cnt] = True
            a, b = map(float, nums)
            if op == "buy":
                records[cnt] = (0, a, b)
            else:
                records[cnt] = (1, a, b)
    except EOFError:
        break
s = [records[i] for i in range(1, cnt + 1) if st[i]]

tot = 0
price = 0


def cal(u):
    global tot, price
    buy = sell = 0
    for tp, p, c in s:
        if tp == 0:
            if p >= u:
                buy += c
        elif tp == 1:
            if p <= u:
                sell += c
    if min(buy, sell) > tot:
        tot = min(buy, sell)
        price = u
    elif min(buy, sell) == tot:
        price = max(price, u)


for i in range(len(s)):
    p = s[i][1]
    cal(p)
print("%.2f" % price, int(tot))











