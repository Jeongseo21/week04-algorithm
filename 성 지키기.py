N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))
col = [0]*M

for i in range(N):
    for j in range(M):
        if graph[i][j] != '.':
            if not col[j]:
                col[j] = 1
print(col.count(0))