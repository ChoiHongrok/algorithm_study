'''
https://www.acmicpc.net/problem/15652
'''

import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

def dfs(start, log, cnt):
    if cnt == M:
        print(log)
    else:
        for n in range(start, N+1):
            dfs(n, log+f' {n}', cnt+1)

for start in range(1, N+1):
    dfs(start, f'{start}', 1)