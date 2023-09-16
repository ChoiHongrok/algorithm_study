'''
https://www.acmicpc.net/problem/23309
'''
import sys
from collections import deque

def found(i, j, dir, que):
    if dir=='N':
        while True:
            pop = que.popleft()
            que.append(pop)
            if pop == i:
                que.append(j)
                pop = que.popleft()
                print(pop)
                que.append(pop)
                break
    elif dir=='P':
        while True:
            pop = que.pop()
            que.appendleft(pop)
            if pop == i:
                que.appendleft(j)
                pop = que.pop()
                print(pop)
                que.appendleft(pop)
                break
            
def remove(i, j, dir, que):
    if dir=='N':
        while True:
            pop = que.popleft()
            que.append(pop)
            if pop == i:
                pop = que.popleft()
                print(pop)
                break
    elif dir=='P':
        while True:
            pop = que.pop()
            que.appendleft(pop)
            if pop == i:
                pop = que.pop()
                print(pop)
                break

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

que = deque(input().strip().split())
location = {sta:i for i, sta in enumerate(que)}
n_sta = len(que)

for m in range(M):
    command = input().strip().split()
    if len(command) > 2:
        com, i, j = command
    else:
        com, i = command
    if com[0] == "B":
        found(i, j, com[1], que)
    elif com[0] == "C":
        remove(i, j, com[1], que)