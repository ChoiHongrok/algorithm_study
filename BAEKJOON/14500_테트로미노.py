'''
https://www.acmicpc.net/problem/14500
'''

import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
mat = []
max_mat = 0
for i in range(N):
    row = list(map(int, input().strip().split()))
    max_mat = max(max_mat, max(row))
    mat.append(row)


min_i, max_i = 0, N-1
min_j, max_j = 0, M-1
 
def dfs(i, j, size, cum_sum, log):
    if max_sum >= cum_sum + max_mat * (5 - size):
        return 0
    if visited[i][j] == True:
        return 0
    visited[i][j] = True
    cum_sum += mat[i][j]
    log += f'({mat[i][j]}) '
    if size == 4:
        # print(f'{log}, {cum_sum}')
        # [print(row) for row in visited]
        visited[i][j] = False
        return cum_sum
    
    max_ret_sum = 0
    if i > min_i:
        ret_sum = dfs(i-1, j, size+1, cum_sum, log+'상')
        max_ret_sum = max(max_ret_sum, ret_sum)
    if i < max_i:
        ret_sum = dfs(i+1, j, size+1, cum_sum, log+'하')
        max_ret_sum = max(max_ret_sum, ret_sum)
    if j > min_j:
        ret_sum = dfs(i, j-1, size+1, cum_sum, log+'좌')
        max_ret_sum = max(max_ret_sum, ret_sum)
    if j < max_j:
        ret_sum = dfs(i, j+1, size+1, cum_sum, log+'우')
        max_ret_sum = max(max_ret_sum, ret_sum)
    visited[i][j] = False
    return max_ret_sum


def cacl_o(i, j):
    sides = [0, 0, 0, 0]
    cnt = 0
    if i > min_i:
        sides[0] = mat[i-1][j]
        cnt += 1
    if i < max_i:
        sides[1] = mat[i+1][j]
        cnt += 1
    if j > min_j:
        sides[2] = mat[i][j-1]
        cnt += 1
    if j < max_j:
        sides[3] = mat[i][j+1]
        cnt += 1
    if cnt < 3:
        return 0
    max_val = 0
    val_sum = sum(sides)
    for k in range(4):
        new_val = val_sum - sides[k]
        max_val = max(new_val, max_val)
        # print(f'{sides}, i: {i}, j:{j}, val:{new_val}')
    return max_val + mat[i][j]
    
        
max_sum = 0
visited = [[False for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        # print(f'>>>>>>i:{i}, j:{j}, max_sum: {max_sum}')
        _sum = dfs(i, j, size=1, cum_sum=0, log='')
        # print(f'_sum: {_sum}')
        max_sum = max(max_sum, _sum)
        _sum = cacl_o(i, j)
        # print(f'_sum: {_sum}')
        max_sum = max(max_sum, _sum)
print(max_sum)