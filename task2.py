def multi(num, length):
    l = []
    for i in range(1, length + 1):
        l.append(num * i)
    return l


print(multi(7, 5))
print(multi(12, 10))
print(multi(17, 6))
