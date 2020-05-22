#!/usr/bin/env python
"""sieve_of_eratosthenes.py

A Python implementation of the Sieve of Eratosthenes."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import random

def sieve(n):
    ints = [x for x in range(2, n+1)]
    primes = []
    p = 2
    while(ints):
        for x in range(1, n/p+1):
            # remove multiples
            if p*x in ints:
                ints.remove(p*x)
        # remove prime
        primes.append(p)
        # find next prime
        if(ints):
            p = ints[0]
    return primes


def main():
    n = random.randint(100, 800)
    primes = sieve(n)
    print("Random n: {}\n".format(n))
    print("Primes: {}\n".format(primes))

if __name__ == "__main__":
    main()


