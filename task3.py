def sum_odd_and_even(lis):
    sEven = 0
    sOdd = 0
    res = []
    for i in lis:
        if i % 2 == 0:
            sEven += i
        else:
            sOdd += i
    res = [sEven, sOdd]
    return res


print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))
