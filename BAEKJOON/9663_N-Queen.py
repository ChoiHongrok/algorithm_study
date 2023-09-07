'''
https://www.acmicpc.net/problem/9663
'''
import sys

def dfs(i, cnt):
    # global _call
    
    # _call += 1
    if i == N:
        # print(board)
        return cnt + 1
    
    for j in range(N):
        if visited[j]:
            continue
        
        if check_cond(i, j):
            board[i] = j
            visited[j] = True
            cnt = dfs(i+1, cnt)    
            board[i] = None
            visited[j] = False
        
    return cnt


def check_cond(i, j):
    # global _call
    for _i in range(i):
        # _call += 1
        if (board[_i] == j) or i-_i == abs(board[_i] - j):
            return False
    return True 
        
input = sys.stdin.readline
N = int(input().rstrip())
board = [None for _ in range(N)]
visited = [False for _ in range(N)]
# _call = 0
ans = dfs(0, 0)
print(ans)
# print(f'_call: {_call}')