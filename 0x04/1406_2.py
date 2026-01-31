import sys
input = sys.stdin.readline

MX = 1000005
dat = [''] * MX
pre = [-1] * MX
nxt = [-1] * MX
unused = 1

def insert(addr, ch):
    global unused
    dat[unused] = ch
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1

def erase(addr):
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]
    nxt[pre[addr]] = nxt[addr]

def traversal():
    cur = nxt[0]
    res = []
    while cur != -1:
        res.append(dat[cur])
        cur = nxt[cur]
    print(''.join(res))

init = input().strip()
cursor = 0
for x in init:
    insert(cursor, x)
    cursor = nxt[cursor]

q = int(input())
for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'P':
        insert(cursor, cmd[1])
        cursor = nxt[cursor]
    elif cmd[0] == 'L':
        if pre[cursor] != -1:
            cursor = pre[cursor]
    elif cmd[0] == 'D':
        if nxt[cursor] != -1:
            cursor = nxt[cursor]
    else:
        if (pre[cursor] != -1):
            erase(cursor)
            cursor = pre[cursor]

traversal()