def dfs(g, v):
    for u in g[v]:
        if not(used[u]):
            used[u] = 1
            dfs(g, u)

n = int(input())
m = int(input())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
used = [0]*n
used[0] = 1
dfs(g, 0)
f = 0
for i in used:
    if not(i):
        f = 1
if f:
    print("NO")
else:
    print("YES")