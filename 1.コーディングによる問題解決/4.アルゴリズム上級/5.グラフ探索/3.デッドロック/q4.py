from collections import deque

N, M = [int(i) for i in input().split()]
G = [[] for _ in range(N)]

# dependent_num
dep_num = [0] * N
for _ in range(M):
    a, b = [int(i) for i in input().split()]
    G[a].append(b)
    dep_num[b] += 1

# seen flag isn't required: because nodes must be checked more than once.
# used_as_roots flag is required: because it tells the zero node is new or not.
used_as_root = [False] * N
q = deque()


def find_new_zeros() -> list:
    zeros = []
    for n, num in enumerate(dep_num):
        if used_as_root[n]:
            continue
        if num == 0:
            zeros.append(n)
    return zeros


q.extend(find_new_zeros())

while q:
    n = q.popleft()
    for ch in G[n]:
        dep_num[ch] -= 1
    used_as_root[n] = True
    # append new zeros AFTER the queue gets empty
    if not q:
        q.extend(find_new_zeros())

if dep_num.count(0) == len(dep_num):
    print("Yes")
else:
    print("No")
