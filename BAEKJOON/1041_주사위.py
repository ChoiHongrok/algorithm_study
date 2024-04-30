'''
https://www.acmicpc.net/problem/1041
'''
import sys
input = sys.stdin.readline

N = int(input())
DICE = list(map(int, input().split()))
if N == 1:
    print(21-max(DICE))
    exit(0)
candid = set(i for i in range(6))
oppo = {0:5, 1:4, 2:3, 3:2, 4:1, 5:0}
minimum = [float('inf'), float('inf'), float('inf')]
first_max = 0

for i in range(3):
    min_idx = -1
    for idx in candid:
        num = DICE[idx]
        if num < minimum[i]:
            min_idx = idx
            minimum[i] = num
        elif i == 0 and num == minimum[i]:
            if DICE[oppo[min_idx]] < DICE[oppo[idx]]:
                min_idx = idx
                minimum[i] = num

    oppo_idx = oppo[min_idx]
    candid.remove(oppo_idx)
    candid.remove(min_idx)

face = [0, (N-2)*(N-2)*5 + (N-2)*4, (N-1)*4 + (N-2)*4, 4]
answer1 = face[1] * minimum[0]
answer2 = face[2] * (minimum[0] + minimum[1])
answer3 = face[3] * (minimum[0] + minimum[1] + minimum[2])
print(answer1 + answer2 + answer3)
'''
N=1, 1면 - 5개 가장 작은 값 제외
N=2, 2면 - 4개 // 3면 - 4개
N=3, 1면 - (3-2)(3-2)*5+(3-2)*4 개 // 2면 - 4*2+4개 // 3면-4개 
N=4, 1면 - (4-2)(4-2)*5+(4-2)*4 // 2면 - 4*3+4*2개 // 3면-4개
N=5, 1면 - // 2면 - 4*4+4*3개// 3면 - 4개
일반식 N=N(N>1), 1면 - (N-2)(N-2)*5+(N-2)*4 // 2면 - (N-1)*4+(N-2)*4개 // 3면 - 4개 
'''