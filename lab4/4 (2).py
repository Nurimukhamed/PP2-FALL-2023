s = [int(x) for x in input().split()]
s_new = set()
for x in s:
    if x in s_new:
        print('YES')
    else:
        print('NO')
        s_new.add(x)