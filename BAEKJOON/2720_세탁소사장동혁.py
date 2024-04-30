'''
https://www.acmicpc.net/problem/2720
'''
import sys
input = sys.stdin.readline

N = int(input())
answer = ''
for _ in range(N):    
    C = int(input())
    for coin in [25, 10, 5, 1]:
       quotient = C // coin
       C = C % coin
       end = '\n' if coin == 1 else ' '
       answer += f'{quotient}{end}'

print(answer)