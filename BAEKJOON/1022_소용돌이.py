import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().strip().split())

def get_value(i, j): # 2, 2
    level = max(abs(i), abs(j)) # 2
    side = 2*level # 4
    end_point = (side+1)**2 #25

    if i == j == level:
        return end_point
    if j  == level:
        return end_point - 4*side + (level-i)  # 25 - 16 + 0 = 9
    elif j == -level:
        return end_point - 2*side + (i+level) # 49 - 12 + (-3+3) = 37
    if i == -level:
        return end_point - 3*side + (level - j) # 9 - 6 +(1-0) = 4
    elif i == level:
        return end_point - side + (j+level) 

mat = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
_max = 0
for mat_i, i in enumerate(range(r1, r2+1)):
    for mat_j, j in enumerate(range(c1, c2+1)):
        val = get_value(i, j)
        _max = max(val, _max)
        mat[mat_i][mat_j] = val

n_digit = len(str(_max))
for row in mat:
    for val in row:
        val_str = str(val)
        space_size = n_digit-len(val_str)
        print(' '*space_size + val_str, end=' ')
    print()