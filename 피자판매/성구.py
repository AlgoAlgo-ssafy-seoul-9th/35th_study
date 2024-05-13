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
