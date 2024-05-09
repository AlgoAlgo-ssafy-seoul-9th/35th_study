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