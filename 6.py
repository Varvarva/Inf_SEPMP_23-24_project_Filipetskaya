def bfs():
    while(len(q) > 0) :
        v = q[0]
        q.pop(0)
        for u in g[v]:
            if not(used[u]):
                used[u] = 1
                q.append(u)
                cnt[u] = cnt[v]+1



n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
cnt = [0]*n
used = [0]*n
q = [0]
used[0] = 1
bfs()
for el in cnt:
    print(el)