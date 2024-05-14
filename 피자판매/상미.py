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
