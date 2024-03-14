def bfs():
    while(len(q) > 0) :
        v = q[0]
        q.pop(0)
        for u in ([v[0]-1, v[1]], [v[0]+1, v[1]], [v[0], v[1]-1], [v[0], v[1]+1]):
            if u[0] >= 0 and u[0] < n  and u[1] >= 0 and u[1] < m:
                if a[u[0]][u[1]] == ' ':
                    if not(used[u[0]][u[1]]):
                        used[u[0]][u[1]] = 1
                        q.append(u)
                        cnt[u[0]][u[1]] = cnt[v[0]][v[1]]+1



n, m = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a = []
for i in range(n):
    a.append(input())

cnt = [[-1]*m for i in range(n)]
used = [[0]*m for i in range(n)]
q = [[x1, y1]]
used[x1][y1] = 1
cnt[x1][y1] = 0
bfs()
if cnt[x2][y2] == -1:
    print("INF")
else:
    print(cnt[x2][y2])