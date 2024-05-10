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

