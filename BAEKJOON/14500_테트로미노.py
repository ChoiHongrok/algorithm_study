'''
https://www.acmicpc.net/problem/14500
'''

import sys

N, M = map(int, sys.stdin.readline().strip().split())
print(1)
mat = []
for i in range(N):
    row = sys.stdin.readline().strip().split()
    mat.append(row)
