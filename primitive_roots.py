from sys import argv

def is_primitive_root(a: int, p: int) -> bool:
    results: set = set()

    for i in range (0, p-1):
        results.add(a**i % p)

    results = sorted(results)
    prev: int = 0

    for n in results:
        if n != (prev + 1):
            return False

        prev = n

    return True


def is_discrete_log(a: int, p: int, x:int) -> bool:
    y: int = a**x % p

    if y < p:
        return True

    return False


def main():
    a: int = int(argv[1])
    p: int = int(argv[2])

    print(is_primitive_root(a, p))

    exit(0)


if __name__ == "__main__":
    main()

