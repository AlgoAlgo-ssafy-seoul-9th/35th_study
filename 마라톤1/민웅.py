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
