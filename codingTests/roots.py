def isPower(a):
    roots = a
    if a == 1:
        return True
    elif a % 2 != 0:
        return False
    else:
        while roots > 2:
            roots = roots/2
        if roots == 2:
            return True
        else:
            return False


print(isPower(10))