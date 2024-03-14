def dfs(g, v, t):
    for u in g[v]:
        if (used[u[0]] == 0):
            used[u[0]] = t

n, m = map(int, input().split())
g = [[] for i in range(n)]
used = [0]*n
for i in range(m):
    a, b, w = map(int, input().split())
    g[a].append([b, w])
    g[b].append([a, w])
ans = []
t = 0
for i in range(n):
    if not(used[i]):
        t += 1
        used[i] = t
        dfs(g, i, t)
ans = [0]*t
for i in range(n):
    for u in g[i]:
        ans[used[i]-1] += u[1]
for i in range(t):
    ans[i] //= 2
ans = sorted(ans)
for i in ans:
    print(i)