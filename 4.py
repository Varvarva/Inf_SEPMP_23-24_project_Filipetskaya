def dfs(v):
    f = 0
    for u in g[v]:
        if f > 0:
            return 1
        if color[u] == 1:
            return 1
        if color[u] == 0:
            color[u] = 1
            f += dfs(u)
    color[v] = 2
    ans.append(v)
    return (f>0)

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
color = [0]*n
f = 0
ans = []
for i in range(n):
    if f > 0:
        break
    if color[i] == 0:
        color[i] = 1
        f += dfs(i)
ans = ans[::-1]
if f == 0:
    print(*ans)
else:
    print("NO")