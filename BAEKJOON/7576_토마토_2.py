'''
https://www.acmicpc.net/problem/7576
'''
import sys
from collections import deque
input = sys.stdin.readline

def left(i, j):
    if j > 0:
        return i, j-1
def right(i, j):
    if j < M-1:
        return i, j+1
def up(i, j):
    if i > 0:
        return i-1, j
def down(i, j):
    if i < N-1:
        return i+1, j

M, N = map(int, input().rstrip().split())
box = [input().rstrip().split() for i in range(N)]

que = deque()
unripe = 0
infection = 0
# [print(row) for row in box]
for i, row in enumerate(box):
    for j, cell in enumerate(row):
        if cell == "1":
            que.append((i, j, 0))
            box[i][j] = '0'
            infection-=1
        if cell == "0":
            unripe += 1

while que:
    # print(que)
    i, j, day = que.popleft()
    status = box[i][j]
    if status == '0':
        infection += 1
        if unripe == infection:
            break
        box[i][j] = '1'
        # print(f'----------{(i, j, day)}--------------')
        # [print(row) for row in box]
        # print('------------------------')
        locs = [left(i, j), right(i, j), up(i, j), down(i, j)]
        for loc in locs:
            if loc:
                ni, nj = loc
                if box[ni][nj] == "0":
                    que.append((ni, nj, day+1))    
                    # print(f'now: {(i, j ,day)} --> {(ni, nj, day+1)}')
                
# print(f'unripe: {unripe}')
# print(f'infection: {infection}')
if unripe == 0:
    print(0)
elif unripe == infection:
    print(day)
else:
    print(-1)