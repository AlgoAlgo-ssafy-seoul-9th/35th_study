# 2174_로봇 시뮬레이션_Robot simulation
import sys
input = sys.stdin.readline
dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
direction = {'E': 0, "N": 1, "W": 2, "S": 3}

A, B = map(int, input().split())
field = [[0]*A for _ in range(B)]

N, M = map(int, input().split())
robots = {}
ans = "OK"

for i in range(1, N+1):
    x, y, d = input().split()
    x, y = int(x), int(y)
    robots[i] = ([B-y, x-1, direction[d]])
    field[B-y][x-1] = i

for _ in range(M):
    r, o, v = input().split()
    r, v = int(r), int(v)

    x, y, d = robots[r]
    nx = x
    ny = y
    if o == "F":
        for i in range(v):
            nx = nx + dxy[d][0]
            ny = ny + dxy[d][1]
            if 0 <= nx <= B-1 and 0 <= ny <= A-1:
                if field[nx][ny]:
                    ans = f"Robot {r} crashes into robot {field[nx][ny]}"
                    break
            else:
                ans = f"Robot {r} crashes into the wall"
                break
        else:
            robots[r] = [nx, ny, d]
            field[nx][ny] = r
            field[x][y] = 0
    elif o == "L":
        d = (d+v)%4
        robots[r] = [x, y, d]
    else:
        d = (d-v)%4
        robots[r] = [x, y, d]

    if ans != "OK":
        break

print(ans)