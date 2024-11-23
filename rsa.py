import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # Get a list of primes from the interval [lo, hi).
    primes = _primes(lo, hi)

    # Sample two distinct primes p and q from primes.
    p, q = _sample(primes, 2)

    # Set n and m to pq and (p-1)(q-1), respectively.
    n = p * q
    m = (p - 1) * (q - 1)

    # Get a list of primes from the interval [2, m).
    primes = _primes(2, m)

    # Choose a random prime e from primes such that e does not divide m.
    e = _choice(primes)
    while m % e == 0:
        e = _choice(primes)

    # Find a d from the interval [1, m) such that ed mod m = 1.
    for d in range(1, m):
        if e * d % m == 1:

            # Return the tuple (n, e, d).
            return (n, e, d)


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    # Return x^e mod n.
    return x ** e % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # Return y^d mod n.
    return y ** d % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # Declare empty list that will store all prime numbers from the
    # interval [lo, hi).
    primes = []

    for p in range(lo, hi):
        # for each p from [lo, hi)...

        # If p is 0 or 1, p is not prime, continue to next iteration.
        if p <= 1:
            continue

        # Set j (potential divisor of p) to 2.
        j = 2

        while j <= p / j:
            # As long as j is less than or equal to p / j...

            if p % j == 0:
                # If j divides p, break (p is not prime).
                break

            # Increment j by 1.
            j += 1

        # If you got here by exhausting the while loop, p is a prime, so
        # append it to primes.
        if j > p / j:
            primes += [p]

    # Return primes.
    return primes


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # Create an empty list b.
    b = []

    # Set b to be a copy of a.
    for val in a:
        b += [val]

    for i in range(k):
        # For the first k elements of a...

        # Generate a random number from the interval [0, len(b)).
        rand = stdrandom.uniformInt(0, len(b))

        # Swap elements at b[i] with b[rand].
        temp = b[i]
        b[i] = b[rand]
        b[rand] = temp

    # Create an empty list chosenPrimes and set it to the first
    # k elements in b.
    chosenPrimes = []
    for i in range(k):
        chosenPrimes += [b[i]]

    # Return chosenPrimes.
    return chosenPrimes


# Returns a random item from the list a.
def _choice(a):
    # Get a random number r from the interval [0, l), where l is
    # the number of elements in a.
    r = stdrandom.uniformInt(0, len(a))

    # Return the element in a at the index r.
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()