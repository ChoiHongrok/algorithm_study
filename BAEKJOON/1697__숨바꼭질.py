'''
https://www.acmicpc.net/problem/1697
'''

from collections import deque


def forward(x, depth):
    return x+1, depth+1


def backward(x, depth):
    return x-1, depth+1


def jump(x, depth):
    return 2*x, depth+1


if __name__ == "__main__":
    N, K = map(int, input().split())
    q = deque()
    d = deque()
    visited = [0 for _ in range(100002)]
    q.append(N)
    d.append(0)

    while q:
        loc = q.popleft()
        depth = d.popleft()
        if not 0 <= loc <= 100001:
            continue
        if visited[loc] == 1:
            continue
        else:
            visited[loc] = 1

        if loc == K:
            print(depth)
            break

        for func in [forward, jump, backward]:
            new_loc, new_depth = func(loc, depth)
            q.append(new_loc)
            d.append(new_depth)
