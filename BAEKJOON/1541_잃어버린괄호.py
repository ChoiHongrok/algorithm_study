import sys

input = sys.stdin.readline

eq = input()
print(eval('-'.join([str(sum(map(int, min_eq.split('+')))) for min_eq in eq.split('-')])))
'''
+먼저 계산하고 -계산.
-는 앞에서부터 계산해야 값이 최소가 됨.
+ - : 1 + 2 - 3 / 2-3 + 1
- + :+ -> -
- - :3-2-2 1-2 / 3-0 2-4-5 -2-5 2+1
+ + : 동일
'''