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
```

### [상미](./무기%20공학/상미.py)

```py

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
