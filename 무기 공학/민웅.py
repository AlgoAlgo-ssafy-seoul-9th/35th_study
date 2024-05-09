# 18430_무기공학
import sys
input = sys.stdin.readline
dxy = [[(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)], [(1, 0), (0, 1)]]


def bt(x, y, v, score):
    global ans

    if y == M:
        x = x+1
        y = 0

    if x == N and y == 0:
        if score > ans:
            ans = score
        return

    if not v[x][y]:
        for ds in dxy:
            tmp = []
            tmp_cordi = []
            for d in ds:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx <= N-1 and 0 <= ny <= M-1 and not v[nx][ny]:
                    tmp.append(woods[nx][ny])
                    tmp_cordi.append([nx, ny])
                else:
                    break
            else:
                tmp_score = sum(tmp) + 2*woods[x][y]
                for c in tmp_cordi:
                    v[c[0]][c[1]] = 1
                v[x][y] = 1
                bt(x, y+1, v, tmp_score+score)
                v[x][y] = 0
                for c in tmp_cordi:
                    v[c[0]][c[1]] = 0
    bt(x, y+1, v, score)


N, M = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
ans = 0

bt(0, -1, visited, 0)

print(ans)