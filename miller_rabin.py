from random import randint


def miller_rabin(n: int, t: int) -> bool:
    # n is odd, n ≥ 3, t ≥ 1
    if n % 2 == 0 or n < 3:
        return False

    if t < 1:
        return False

    r: int
    s: int

    # (n - 1) = 2^s*r
    for i in range(int((n-1)/2)):
        s = i
        r = int((n - 1) / (2 ** s))

        if r % 2 != 0:
            break

    # Generate random int 2 ≤ a ≤ n-2
    a: int = randint(2, n - 2)

    y: int = a ** r % n

    if y != 1 and y != (n - 1):
        j: int = 1

        while j <= s - 1 and y != (n - 1):
            y = y ** 2 % n

            if y == 1:
                return False

            j += 1

        if y != (n - 1):
            return False

    return True


def main():
    n: int = 91
    t: int = 3

    print(miller_rabin(n, t))

    exit(0)


if __name__ == '__main__':
    main()
