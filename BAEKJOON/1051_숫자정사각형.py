'''
https://www.acmicpc.net/problem/1051
'''
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
mat = []


for i in range(N):
    row = list(map(int, input().strip()))
    mat.append(row)

size = min(N, M)

while True:
    for i in range(N-size+1):
        for j in range(M-size+1):
            vertex1 = mat[i][j]
            vertex2 = mat[i][j+size-1]
            vertex3 = mat[i+size-1][j]
            vertex4 = mat[i+size-1][j+size-1]

            if vertex1 == vertex2 == vertex3 == vertex4:
                print(size**2)
                exit(0)
    size -= 1