num=int(input())
if num >1:
    for i in range (2,int(num/2)+1):
        if (num%1)==0:
            print(num, "not prime")
            break
    else:
        print(num,"is prime")
else:
    print(num, "is not prime")

def generate_primes(n):
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    primes = []

    # Start with the smallest prime number, 2.
    p = 2
    while p * p <= n:
        # If is_prime[p] is not changed, then it is a prime.
        if is_prime[p]:
            # Update all multiples of p.
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Append all prime numbers to the 'primes' list.
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)

    return primes


# Example usage
n = int(input("Enter a number (n): "))
primes = generate_primes(n)
print("Prime numbers up to", n, "are:")
print(primes)
