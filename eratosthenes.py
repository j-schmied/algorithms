from math import sqrt
from sys import argv


def sieve_of_eratosthenes(upper_limit: int) -> list:
    primes: list = list()

    # Fill list with values from 2 to upper_limit
    for i in range(2, upper_limit + 1):
        primes.append(i)

    sieving_limit = int(sqrt(upper_limit))

    for n in range(2, sieving_limit + 1):
        for i in primes:
            if i % n == 0:
                if i != n:
                    primes.remove(i)

    return primes


def main():
    range: int = int(argv[1])

    print(sieve_of_eratosthenes(range))

    exit(0)


if __name__ == '__main__':
    main()

