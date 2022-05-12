'''
https://www.acmicpc.net/problem/7576
'''
from collections import deque


def left(w, h):
    return w-1, h


def right(w, h):
    return w+1, h


def up(w, h):
    return w, h-1


def down(w, h):
    return w, h+1


if __name__ == "__main__":
    W, H = map(int, input().split())
    toms = []
    q = deque()
    reap = 1
    for h in range(H):
        w_lst = []
        for w, v in enumerate(input().split()):
            if v == '0':
                reap = 0
            if v == '1':
                q.append((w, h, 0))
            w_lst.append(v)
        toms.append(w_lst)

    if reap: # 모든 토마토가 익어있는 상태
        print(0)
        exit(0)

    visited = [[0 for _ in range(W)] for _ in range(H)]

    max_days = 0

    while q:
        now_w, now_h, depth = q.popleft()
        if now_w < 0 or now_h < 0 or now_w >= W or now_h >= H:
            continue
        if visited[now_h][now_w] == 1:
            continue
        else:
            visited[now_h][now_w] = 1

        tom_state = toms[now_h][now_w]
        if tom_state == '-1':
            continue
        else:
            max_days = max(max_days, depth)
            for step in [left, right, up, down]:
                next_w, next_h = step(now_w, now_h)
                q.append((next_w, next_h, depth+1))

    for h, row in enumerate(visited):
        for w, tom in enumerate(row):
            if not tom and toms[h][w] != "-1": # 토마토가 모두 익지는 못하는 상태
                print(-1)
                exit(0)

    print(max_days)