# sol1
def p_lines(l1, l2):
    if l2[1] / l2[0] == l1[1] / l1[0]:
        return True
    else:
        return False


print(p_lines([1, 2, 3], [1, 2, 4]))
print(p_lines([2, 4, 1], [4, 2, 1]))
print(p_lines([0, 1, 5], [0, 1, 5]))

 