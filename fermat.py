from euklid import euklid_ggT


def fermat_prime_test(p: int, g: int) -> bool:
    if euklid_ggT(p, g) != 1:
        return False

    y: int = g ** (p - 1) % p

    return y == 1


def main():
    a: int = 3
    b: int = 5
    c: int = 10

    print(fermat_prime_test(a, b))
    print(fermat_prime_test(b, c))

    exit(0)


if __name__ == '__main__':
    main()
