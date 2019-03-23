n = int(input('enter the number of queens'))
col = []
for i in range(n+1):
    col.append(0)
q = 1


def isSafe(r, c):
    for i in range(1, r):
        if c == col[i] or abs(c - col[i]) == abs(i - r):
            return 0
    return 1

def nQueen(q):
    global col
    flag = 1
    for c in range(1, n+1):
        if isSafe(q, c):
            col[q] = c
            if q == n:
                for e in col[1:]:
                    if e == 0:
                        flag = 0
                if flag != 0:
                    print(col)
            else:
                nQueen(q+1)

nQueen(q)