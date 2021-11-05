def snakefill(n):
    s = 1
    cnt = 0
    while s < n * n - s:
        s = s * 2
        cnt += 1
    return cnt


print(snakefill(3))
print(snakefill(5))
print(snakefill(24))

