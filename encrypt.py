import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept public-key n (int) and e (int) as command-line arguments.
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Set width to the number of bits needed to encode n.
    width = rsa.bitLength(n)

    # Accept string message to encrypt from standard input.
    message = stdio.readAll()

    for c in message:
        # For each character c in message....

        # Turn c into an integer x.
        x = ord(c)

        # Encrypt x and write the encrypted value as a width-long
        # binary string.
        encryptedVal = rsa.encrypt(x, n, e)
        stdio.write(rsa.dec2bin(encryptedVal, width))

    # Write a newline character.
    stdio.writeln()


if __name__ == '__main__':
    main()