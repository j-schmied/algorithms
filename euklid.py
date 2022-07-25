def euklid_ggT(n: int, a: int) -> int:
    if a > n:
        return euklid_ggT(a, n)

	if a == 0:
		return n

	while a != 0:
		a, n = n % a, a

	return n


def extended_euklid(n: int, a: int):
	c: int
	d: int
	uc: int
	vc: int
	ud: int
	vd: int
	q: int

	c, d = a, n
	uc, vc, ud, vd = 1, 0, 0, 1

	while c != 0:
		q = int(d/c)
		c, d = d - q * c, c
		uc, vc, ud, vd = ud - q * uc, vd - q * vc, uc, vc

	k, v, u = d, vd, ud

    return k, v, u


def main():
	a: int = 3
	b: int = 6
	c: int = 17

	print(euklid_ggT(a, b))
	print(euklid_ggT(b, c))

	print(extended_euklid(c, a))

	exit(0)


if __name__ == '__main__':
	main()

