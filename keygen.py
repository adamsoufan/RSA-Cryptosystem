import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept lo (int) and hi (int) as command-line arguments.
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Generate public/private keys (n, e, d).
    keys = rsa.keygen(lo, hi)

    # Write keys to standard output.
    for v in keys:
        stdio.write(str(v) + ' ')

    stdio.writeln()


if __name__ == '__main__':
    main()