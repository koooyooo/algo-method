N = int(input())
As = [int(i) for i in input().split()]
Bs = [int(i) for i in input().split()]

MAX = 10 ** 7
shortest = [MAX] * N


for i in range(N):
    if i == 0:
        shortest[0] = 0
        continue
    if i == 1:
        shortest[1] = shortest[0] + As[0]
        continue
    path_a = shortest[i-1] + As[i-1]
    path_b = shortest[i-2] + Bs[i-2]
    shortest[i] = min([path_a, path_b])


print(shortest[N-1])
