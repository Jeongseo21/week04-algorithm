# 세로의 크기 M, 가로의 크기 N

M, N = map(int, input().split())

graph = []
visited = [[0]*(N+1) for _ in range(M)]
for _ in range(M):
    graph.append(list(map(int, input().split())))


def dfs(x, y, count):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while x < N and y < M:
        for _ in range(M):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if visited[nx][ny] == 0:
                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        continue
                    if graph[x][y] < graph[nx][ny]:
                        continue
                    if nx == N-1 and ny == M-1:
                        count += 1
                        return count
                    visited[nx][ny] = 1
                    dfs(nx, ny, count)
                    print(visited)


print(dfs(0, 0, 0))