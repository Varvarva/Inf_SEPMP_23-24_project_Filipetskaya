def bfs(t):
    while(len(q) > 0) :
        v = q[0]
        q.pop(0)
        used[v] = t
        for u in g[v]:
            if used[u] == -1:
                used[u] = 0
                q.append(u)
                cnt[u] = cnt[v]+1
                par[u] = v
            elif used[u] == t:
                return [v, u]
    return [-1, -1]



n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
cnt = [0]*n
used = [-1]*n
par = [-1]*n
t = 0
res = []
for i in range(n):
    if used[i] == -1:
        t += 1
        q = [i]
        used[i] = t
        w = bfs(t)
        k = w[0]
        p = w[1]

        if k != -1:
            ans = []
            while k != p and k != -1:
                ans.append(k)
                k = par[k]
            if k != -1:
                ans.append(k)
            ans = ans[::-1]
            if len(res) == 0 or len(res) > len(ans):
                res = ans
if len(res) == 0:
    print("NO CYCLES")
else:
    print(*res)