def solution(n, b):
    ids = []

    while True:
        z = subtract(n, b)

        if z in ids:
            break

        else:
            ids.append(z)
            n = z

    return len(ids) - ids.index(z)


def order(n):
    return int(''.join(sorted(n, reverse=True))), int(''.join(sorted(n)))


def subtract(n, b):
    k = len(n)
    x, y = order(n)

    difference = ""
    borrow = 0

    while x > 0:
        tmp = (x % 10) - (y % 10) + borrow

        if tmp < 0:
            tmp += b
            borrow = -1

        else:
            borrow = 0

        difference += str(tmp)

        x //= 10
        y //= 10

    return (k - len(difference)) * '0' + difference[::-1]


print(solution("210022", 3))
