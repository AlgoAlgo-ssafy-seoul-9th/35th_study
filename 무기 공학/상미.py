import sys
input = sys.stdin.readline

def boomerang1(i, j):
    if i > 0 and j < M - 1 and not visited[i][j] and not visited[i-1][j] and not visited[i][j+1]:
        return (tree[i][j]*2 + tree[i-1][j] + tree[i][j+1], (i, j), (i-1, j), (i, j+1))
    return None

def boomerang2(i, j):
    if i < N - 1 and j < M - 1 and not visited[i][j] and not visited[i+1][j] and not visited[i][j+1]:
        return (tree[i][j]*2 + tree[i+1][j] + tree[i][j+1], (i, j), (i+1, j), (i, j+1))
    return None

def boomerang3(i, j):
    if i < N - 1 and j > 0 and not visited[i][j] and not visited[i+1][j] and not visited[i][j-1]:
        return (tree[i][j]*2 + tree[i+1][j] + tree[i][j-1], (i, j), (i+1, j), (i, j-1))
    return None

def boomerang4(i, j):
    if i > 0 and j > 0 and not visited[i][j] and not visited[i-1][j] and not visited[i][j-1]:
        return (tree[i][j]*2 + tree[i-1][j] + tree[i][j-1], (i, j), (i-1, j), (i, j-1))
    return None

def bt(i, j, tmp):
    global ans
    if j == M:
        j = 0
        i += 1
    if i == N:
        ans = max(ans, tmp)
        return

    for boomerang in [boomerang1, boomerang2, boomerang3, boomerang4]:
        result = boomerang(i, j)
        if result:
            value, p1, p2, p3 = result
            visited[p1[0]][p1[1]] = visited[p2[0]][p2[1]] = visited[p3[0]][p3[1]] = 1
            bt(i, j + 1, tmp + value)
            visited[p1[0]][p1[1]] = visited[p2[0]][p2[1]] = visited[p3[0]][p3[1]] = 0

    bt(i, j + 1, tmp)

N, M = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0

bt(0, 0, 0)
print(ans)
