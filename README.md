# 35th_study

알고리즘 스터디 35주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [마라톤1](https://www.acmicpc.net/problem/10655)

### [민웅](./마라톤1/민웅.py)

```py

```

### [상미](./마라톤1/상미.py)

```py
import sys
input = sys.stdin.readline

N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

totalD = 0
for i in range(1, N):
    totalD += abs(X[i-1]-X[i]) + abs(Y[i-1]-Y[i])

maxD = 0
for i in range(2, N):
    canSave = abs(X[i-2]-X[i-1]) + abs(X[i-1] - X[i]) + abs(Y[i-2]-Y[i-1]) + abs(Y[i-1] - Y[i]) - (abs(X[i-2]-X[i]) + abs(Y[i-2]-Y[i]))
    if maxD < canSave:
        maxD = canSave

ans = totalD - maxD
print(ans)
```

### [성구](./마라톤1/성구.py)

```py
# 10655 마라톤 1
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    checkPoints = [tuple(map(int, input().split())) for _ in range(N)]

    # 거리 계산용
    def distance(x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)

    total = 0       # 스킵 안했을 때 거리
    maxDiffer = -1000000    # 스킵했을 때와 안 했을 때의 최댓값
    for idx in range(1,N-1):
        # 인덱싱
        (previ,prevj), (i,j), (posti,postj) = checkPoints[idx-1], checkPoints[idx], checkPoints[idx+1]
        # 스킵 안 했을 때 거리
        nonSkip = [distance(previ,prevj,i,j), distance(i,j,posti,postj)]
        # 스킵 했을 때 거리
        skipped = distance(previ,prevj,posti,postj)
        maxDiffer = max(sum(nonSkip) - skipped, maxDiffer)
        total += nonSkip[0]
    else:
        # 마지막 거리 포함
        total += nonSkip[1]

    print(total - maxDiffer)

    return


if __name__ == "__main__":
    main()
```

### [영준](./마라톤1/영준.py)

```py

```

<br/>

## [로봇 시뮬레이션](https://www.acmicpc.net/problem/2174)

### [민웅](./로봇%20시뮬레이션/민웅.py)

```py
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
```

### [성구](./로봇%20시뮬레이션/성구.py)

```py

```

### [영준](./로봇%20시뮬레이션/영준.py)

```py

```

<br/>

## [피자판매](https://www.acmicpc.net/problem/2632)

### [민웅](./피자판매/민웅.py)

```py

```

### [상미](./피자판매/상미.py)

```py

```

### [성구](./피자판매/성구.py)

```py

```

### [영준](./피자판매/영준.py)

```py

```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

<br/>

## [무기 공학](https://www.acmicpc.net/problem/18430)

### [민웅](./무기%20공학/민웅.py)

```py
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
```

### [상미](./무기%20공학/상미.py)

```py
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

```

### [성구](./무기%20공학/성구.py)

```py
# 18430 무기 공학
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    log = [list(map(int, input().split())) for _ in range(N)]

    bumerang = [(0,-1,1,0), (-1,0,0,-1), (-1,0,0,1), (1,0,0,1)]

    if N < 2 or M < 2:
        print(0)
        return

    visited = [[0] * M for _ in range(N)]

    def bt(idx, strength, maxv):
        # indexing
        if idx == N*M:
            maxv = max(maxv, strength)
            return maxv

        # i,j unzip
        i,j = idx // M, idx % M
        if not visited[i][j]:   # 이미 사용한 부분은 넘어감
            # 부메랑 만들 수 있는지 판단
            for ly,lx, ry,rx in bumerang:
                ly+= i
                lx+= j
                ry+= i
                rx+= j
                if (
                    0 <= ly < N
                    and 0 <= ry < N
                    and 0 <= lx < M
                    and 0 <= rx < M
                    and not visited[ly][lx]
                    and not visited[ry][rx]
                    ):
                    # 만들 수 있으면 체크하고 다음으로 넘어감
                    visited[ly][lx] = visited[i][j] =  visited[ry][rx] = 1
                    maxv = max(maxv, bt(idx+1, strength+log[i][j] * 2+log[ly][lx]+log[ry][rx], maxv))
                    # 체크했으면 원복
                    visited[ly][lx] = visited[i][j] =  visited[ry][rx] = 0

        maxv = max(maxv, bt(idx+1, strength, maxv))
        return maxv

    print(bt(0, 0, 0))
    return


if __name__ == "__main__":
    main()
```

### [영준](./무기%20공학/영준.py)

```py

```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
