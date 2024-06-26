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
# 10655_마라톤1_marathon1
import sys
input = sys.stdin.readline

def distance(s, e):
    return abs(s[0]-e[0]) + abs(s[1]-e[1])

N = int(input())
checkpoints = [list(map(int, input().split())) for _ in range(N)]
ans = -1
max_skip = 0
total = distance(checkpoints[-1], checkpoints[-2])
for i in range(N-2):
    tmp1 = distance(checkpoints[i], checkpoints[i+1])
    tmp2 = distance(checkpoints[i+1], checkpoints[i+2])
    original = tmp1 + tmp2
    total += tmp1

    skip = distance(checkpoints[i], checkpoints[i+2])
    if original - skip > max_skip:
        max_skip = original - skip

print(total-max_skip)

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
N = int(input())
cp = [list(map(int, input().split())) for _ in range(N)]

# i-1에서 i까지 거리
dis = [0]+[abs(cp[i-1][0]-cp[i][0])+abs(cp[i-1][1]-cp[i][1]) for i in range(1, N)]
# i-2에서 i까지 거리 skip[i]
skip = [0,0]+[abs(cp[i-2][0]-cp[i][0])+abs(cp[i-2][1]-cp[i][1]) for i in range(2, N)]

max_diff = 0
for i in range(2, N):   # i-1을 거쳐건 경우와 건너뛴 경우의 차이가 가장 큰 경우
    if dis[i-1]+dis[i] >= skip[i] and max_diff<dis[i-1]+dis[i] -skip[i]:
        max_diff = dis[i - 1] + dis[i] - skip[i]

print(sum(dis)-max_diff)
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

### [상미](./로봇%20시뮬레이션/상미.py)

```py
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]      # N E S W 시계방향 순서
dy = [1, 0, -1, 0]

def isinArea(x, y):
    if 1 <= x <= A and 1 <= y <= B:
        return True

def move(robot, order, dir):
    global robots
    if order == 'F':
        robots[robot][0] += dx[dir]
        robots[robot][1] += dy[dir]
    elif order == 'L':
        robots[robot][2] = (dir-1) % 4
    elif order == 'R':
        robots[robot][2] = (dir+1) % 4

A, B = map(int, input().split())    # 가로 A, 세로 B
N, M = map(int, input().split())    # 로봇 N개, 명령 M개
robots = []
for _ in range(N):              # i+1번 로봇의 x좌표, y좌표, 방향
    x, y, d = map(str, input().strip().split())
    if d == 'N':
        d = 0
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 2
    else:
        d = 3
    robots.append([int(x), int(y), d])
orders = []
flag = False
for _ in range(M):
    order = list(map(str, input().strip().split()))   # 로봇 번호, 명령, 횟수
    orders.append(order)
for order in orders:
    robotN = int(order[0])
    orderN = int(order[2])
    for i in range(orderN):
        move(robotN-1, order[1], robots[robotN-1][2])
        if not isinArea(robots[robotN-1][0], robots[robotN-1][1]):
            print(f'Robot {robotN} crashes into the wall')
            flag = True
            break
        else:
            pass
        if flag:
            break
        for i in range(N):
            if i != robotN-1:
                if robots[i][0] == robots[robotN-1][0] and robots[i][1] == robots[robotN-1][1]:
                    print(f'Robot {robotN} crashes into robot {i+1}')
                    flag = True
                    break
    if flag:
        break

else:
    print('OK')

```

### [성구](./로봇%20시뮬레이션/성구.py)

```py
# 2174 로봇 시뮬레이션
import sys
input = sys.stdin.readline


def main():
    # input
    A, B = map(int, input().split())
    N, M = map(int, input().split())

    # input settings
    robots = [0]        # 로봇 리스트
    lands = set()       # 로봇 위치 확인용 set
    indexes = {}        # 로봇 인덱스 확인용 dictionary
    for i in range(N):
        x,y,d = input().strip().split()
        x, y = int(x), int(y)
        robots.append((x,y,d))
        lands.add((x,y))
        indexes[(x,y)] = i+1

    orders = []         # 명령 리스트
    for _ in range(M):
        idx, order, repeat = input().strip().split()
        orders.append((int(idx), order, int(repeat)))



    def isCrash(robot_idx, nx, ny): # 충돌 확인
        if nx > A or nx < 1 or ny > B or ny < 1:
            print(f"Robot {robot_idx} crashes into the wall")
            return 1

        if (nx, ny) in lands:
            print(f"Robot {robot_idx} crashes into robot {indexes[(nx,ny)]}")
            return 1

        return 0

    def walk(r_idx, x,y,d,repeat):  # F일 때 움직임
        # 방향별 움직임
        move = {
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0),
            "N": (0, 1)
        }
        nx, ny = x, y
        is_crashed = False      # 충돌난 것 확인용
        for _ in range(repeat):
            nx += move[d][0]
            ny += move[d][1]
            if isCrash(r_idx, nx, ny):
                is_crashed = True
                break

        return (is_crashed, nx, ny)

    def turn(order, d, repeat):     # 방향을 바꿈
        repeat %= 4         # 방향은 4번 돌면 그대로 돌아옴
        direction = ["E", "S", "W", "N"]    # 오른쪽으로 도는 기준 정렬
        # 왼쪽으로 도는 경우는
        # 오른쪽으로 도는 횟수 = (4-왼쪽으로 도는 횟수) 를 만족
        if order == "L":
            repeat = 4 - repeat

        # 방향별 인덱싱
        if d == "E":
            d = 0
        elif d == "S":
            d = 1
        elif d == "W":
            d = 2
        else:
            d = 3

        # 원형 큐 알고리즘을 통한 방향 전환 결과 도출
        d += repeat

        return direction[d % 4]

    # test code
    # test_oder = input().strip()
    # test_d = input().strip()
    # test_repeat = int(input())
    # print(turn(test_oder, test_d, test_repeat))

    # 명령 수행 반복문
    for robot_idx, order, repeat in orders:
        x, y, d = robots[robot_idx]
        if order == "F":
            # 이미 충돌이 났으면 그 뒤에 탐색할 필요없음
            is_crashed, candx, candy = walk(robot_idx,x,y,d,repeat)
            if is_crashed:
                break

            # 충돌이 안 났으면 변수들 초기화
            robots[robot_idx] = (candx, candy, d)   # 로봇 위치 초기화
            lands.discard((x,y))                    # 로봇 위치 확인용 set 초기화
            lands.add((candx, candy))
            indexes.pop((x,y))                      # 로봇 인덱스 확인용 dictionary 초기화
            indexes[(candx, candy)] = robot_idx
        else:
            # 방향만 바꾸는 경우는 충돌이 날 확률이 없음
            # 방향 전환 후 로봇 방향 초기화
            cand = turn(order, d, repeat)
            robots[robot_idx] = (x, y, cand)
    else:
        # 모두 이상 없으면 OK 출력
        print("OK")

    return


if __name__ == "__main__":
    main()


```

### [영준](./로봇%20시뮬레이션/영준.py)

```py

```

<br/>

## [피자판매](https://www.acmicpc.net/problem/2632)

### [민웅](./피자판매/민웅.py)

```py
# 2632_피자판매_selling pizza
import sys
input = sys.stdin.readline

size = int(input())

M, N = map(int, input().split())

p1 = [int(input()) for _ in range(M)]
p1_sum = sum(p1)
for i in range(M):
    p1.append(p1[i])

p2 = [int(input()) for _ in range(N)]
p2_sum = sum(p2)
for i in range(N):
    p2.append(p2[i])

p1_case = {}

for i in range(M):
    tmp = 0
    for j in range(i, i+M):
        tmp += p1[j]
        if tmp > size:
            break

        if tmp not in p1_case.keys():
            p1_case[tmp] = 1
        else:
            p1_case[tmp] += 1

p1_case[p1_sum] = 1

ans = 0
if size in p1_case.keys():
    ans += p1_case[size]

for i in range(N):
    tmp = 0
    for j in range(i, i+N):
        tmp += p2[j]
        if tmp == size and size != p2_sum:
            ans += 1
        if tmp == p2_sum:
            continue
        elif (size - tmp) in p1_case.keys():
            ans += p1_case[(size-tmp)]
        if tmp >= size:
            break
if size == p2_sum:
    ans += 1

if (size-p2_sum) in p1_case.keys():
    ans += p1_case[(size-p2_sum)]

print(ans)

```

### [상미](./피자판매/상미.py)

```py
## 12퍼

import sys
input = sys.stdin.readline

want = int(input())
A, B = map(int, input().split())
pizzaA = [int(input()) for _ in range(A)]
pizzaB = [int(input()) for _ in range(B)]

def pizzaPcs(pizza):
    size = len(pizza)
    pizza = pizza + pizza
    sizeDict = {0: 1}
    for start in range(size):
        pcs = 0
        for end in range(start, start+size):
            pcs += pizza[end]
            if pcs > want:
                break
            sizeDict[pcs] = sizeDict.get(pcs, 0) + 1
    return sizeDict

ADict = pizzaPcs(pizzaA)
BDict = pizzaPcs(pizzaB)
ans = 0
for key, value in ADict.items():
        if want - key in BDict:
            ans += BDict[want - key] * ADict[key]

print(ans)

```

### [성구](./피자판매/성구.py)

```py
# 2632 피자판매
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    # INPUT
    needs = int(input())
    m, n = map(int, input().split())
    A, B = [0]*m, [0]*n
    for i in range(m):
        A[i] = int(input())

    for i in range(n):
        B[i] = int(input())

    # SETTINGS
    # 피자 조각을 만들 수 있는 후보 dictionary
    candidate = {
        "A": defaultdict(int),
        "B": defaultdict(int),
    }
    # 답 저장용
    ans = 0

    # 후보군 만드는 함수
    def makeCandidate(cand_name:str, array:list, length:int):
        cnt = 0     # 이미 조건 충족 개수
        fin_num = 0     # 마지막 모두 더한 값
        for i in range(length):
            pieces = 0      # 중간 저장 값
            for j in range(i, length+i):
                if j == length+i-1:     # 만약 모두 더한 값이면 한 번만 저장해야하기에 따로 저장
                    fin_num = pieces+array[j%length]
                    continue

                # 피자 조각 확인 코드
                pieces += array[j%length]
                if pieces < needs:
                    candidate[cand_name][pieces] += 1
                elif pieces == needs:
                    cnt += 1
                    break
                else:
                    break

        if fin_num < needs:
            candidate[cand_name][fin_num] += 1
        elif fin_num == needs:
            cnt += 1

        # 미리 만드는 경우의 수 반환
        return cnt

    # A와 B에 대해 모두 만들기
    ans += makeCandidate("A", A, m)
    ans += makeCandidate("B", B, n)

    # CONFIRM CODE
    # print(candidate, ans)

    # A를 기준으로 (조건 값 - A의 후보군 값 == B의 후보군 값) 성립하는 경우의 수 체크
    for c in candidate["A"]:
        ans += candidate["B"][needs-c] * candidate["A"][c]

    # OUTPUT
    print(ans)

    return


if __name__ == "__main__":
    main()

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
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def f(c, org, p):  # org 남은 목재, p 부메랑들의 강도 합
    global max_v
    if max_v < p:
        max_v = p
    if c>=N*M:
        return
    i = c//M
    j = c%M

    if org[i][j] == 0:     # 중심으로 활용
        for k in range(4):
            dest = [row[:] for row in org]
            ni1, nj1 = i+di[k], j+dj[k]
            ni2, nj2 = i+di[(k+1)%4], j+dj[(k+1)%4]
            if 0<=ni1<N and 0<=nj1<M and 0<=ni2<N and 0<=nj2<M:
                if org[ni1][nj1]==0 and org[ni2][nj2]==0:
                    dest[i][j] = 1
                    dest[ni1][nj1] = 1
                    dest[ni2][nj2] = 1
                    f(c+1, dest, p + arr[i][j]*2+arr[ni1][nj1]+arr[ni2][nj2])
    dest = [row[:] for row in org]
    f(c+1, dest, p)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
used = [[0]*M for _ in range(N)]
if N<2 or M<2:
    print(0)
else:
    max_v = 0
    f(0, used, 0)
    print(max_v)
```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
