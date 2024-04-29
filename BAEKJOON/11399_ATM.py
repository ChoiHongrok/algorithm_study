'''
https://www.acmicpc.net/problem/11399
'''

import sys

input = sys.stdin.readline

N = int(input())
waiting = list(map(int, input().split()))
answer = 0
for time in sorted(waiting):
    answer += time * N
    N -= 1

print(answer)