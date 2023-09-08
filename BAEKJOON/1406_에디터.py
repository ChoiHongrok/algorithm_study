'''
https://www.acmicpc.net/problem/1406
'''

import sys
from collections import deque

input = sys.stdin.readline

line = input().strip()
N = int(input().strip())

left = deque(line)
right = deque()

    
for _ in range(N):
    command = input().strip()
    if command[0] == 'L':
        if len(left) > 0:
            popped = left.pop()
            right.appendleft(popped)
    elif command[0] == 'D':
        if len(right) > 0:
            popped = right.popleft()
            left.append(popped)
    elif command[0] == 'B':
        if len(left) > 0:
            left.pop()
    else:
        left.append(command[2:])
        
for l in left:
    print(l, end='')

for r in right:
    print(r, end='')

