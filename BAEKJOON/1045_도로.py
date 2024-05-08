'''
https://www.acmicpc.net/problem/1045
'''

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

road = []

for _ in range(N):
    road.append(input().split())

