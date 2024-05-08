'''
https://www.acmicpc.net/problem/1052
'''

import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))

binary = bin(N)[2:]
bin_lst = list(map(int, binary))
if sum(bin_lst) <= K:
    full = N
elif binary[:K] == '1' * K:
    full = int('1'+'0'*len(binary), 2)
else:
    full = list(binary)
    cnt = sum(bin_lst)
    for idx, val in enumerate(binary[::-1]):
        if val == '1':
            full[-(idx+1)] = '0'
            cnt -= 1
        if cnt < K and val == '0':
            full[-(idx+1)] = '1'
            break

    full = int(''.join(full), 2)
print(full - N)

'''
정답이 없는 경우: ?
------------------
19 = 16+2+1 = 0b10011
13 = 8+4+1 = 0b1101
9 = 8+1 = 0b1001
59 = 32+16+8+2+1 = 0b111011
36 = 32+4 = 0b100100
43 = 32+8+2+1 = 0b101011 -> 0b101100 -> 0b110000
11 = 8+2+1 = 0b1011
19 = 16+2+1 = 0b10011 
'''