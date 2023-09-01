import sys

# N개의 물건
# W: 무게
# V: 가치
# K: 최대 무게

N, K = map(int, sys.stdin.readline().split())

for i in range(N):
    W, V = map(int, sys.stdin.readline().split())