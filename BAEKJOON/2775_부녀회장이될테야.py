import sys

def sumMember(members, k_i, n_i):
    return members[k_i-1][n_i] + members[k_i][n_i-1]

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    members = [[i+1 for i in range(n)]]

    for k_i in range(1, k+1):
        members.append([1])
        for n_i in range(1, n):
            summed = sumMember(members, k_i, n_i)
            members[k_i].append(summed)

    print(members[k][n-1])