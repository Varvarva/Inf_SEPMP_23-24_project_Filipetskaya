def dfs(v, t):
    low[v] = time[v]
    for u in g[v]:
        if time[u] == 0:
            t += 1
            time[u] = t
            dfs(u, t)
            low[v] = min(low[u], low[v])
        else:
            low[v] = min(low[v], time[u])

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
time = [0]*n
low = [0]*n
ch = [n+1]*n
ans = []
t = 0
for i in range(n):
    if time[i] == 0:
        t += 1
        time[i] = t
        dfs(i, t)
        if (len(g[i]) > 1):
            ans.append(i+1)
        ch[i] = -1
f = 1
for i in range(n):
    for u in g[i]:
        if time[i] == low[u] and ch[i] != -1:
            ans.append(i+1)
            f = 0
            break
if f:
    print(-1)
else:
    ans = sorted(ans)
    print(*ans)