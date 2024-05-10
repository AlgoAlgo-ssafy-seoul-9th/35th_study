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
