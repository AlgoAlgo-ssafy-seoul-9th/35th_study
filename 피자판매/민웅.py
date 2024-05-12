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
