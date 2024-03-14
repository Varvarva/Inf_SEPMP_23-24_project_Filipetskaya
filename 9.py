def bfs():
    while(len(q) > 0) :
        v = q[0]
        q.pop(0)
        for u in ([v[0]-2, v[1]-1], [v[0]-2, v[1]+1], [v[0]+2, v[1]-1], [v[0]+2,v[1]+1],
                  [v[0]-1, v[1]-2], [v[0]+1, v[1]-2], [v[0]+1, v[1]+2], [v[0]-1, v[1]+2]):
            if u[0] >= 0 and u[0] < 8  and u[1] >= 0 and u[1] < 8:
                if not(used[u[0]][u[1]]):
                    used[u[0]][u[1]] = 1
                    q.append(u)
                    cnt[u[0]][u[1]] = cnt[v[0]][v[1]]+1


d = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

k1, k2 = map(str, input().split())
x1 = d[k1[0]]
x2 = d[k2[0]]
y1 = int(k1[1])
y2 = int(k2[1])

cnt = [[-1]*8 for i in range(8)]
used = [[0]*8 for i in range(8)]
q = [[x1, y1]]
used[x1][y1] = 1
cnt[x1][y1] = 0
bfs()
if cnt[x2][y2]%2 == 1:
    print(-1)
else:
    print(cnt[x2][y2]//2)