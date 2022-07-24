from math import sqrt
from eratosthenes import sieve_of_eratosthenes


def euler_phi(n: int) -> int:
	# if n is prime, phi = n - 1
	primes = sieve_of_eratosthenes(n)
	if primes[-1] == n:
		return n - 1
	
	p: int
	q: int
	
	limit: int = int(sqrt(n))
	
	for i in range(2, limit + 1):
		p = i
		if n % p == 0:
			q = int(n / p)
			break
						
	return (p - 1) * (q - 1)
	
	
def euler_theorem(m: int, n: int):
	return m ** euler_phi(n) % n == 1
	

def main():
	n: int = 143
	
	print(euler_phi(143))
	
	a: int = 169
	b: int = 196
	
	print(euler_theorem(a, b))
	
	exit(0)
	

if __name__ == '__main__':
	main()

