#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:31:15 2021

@author: vsriya23
"""

# Assignment 1, question 4


def get_prime_factors(N):
    ''' workflow of fucnction:
        - if N < 10^6, create a list of all prime numbers from 1 to N
        - create a list of numbers from all_primes which are factors of N 
        - return list of prime factors of N '''
    if N < 1000000:
        all_primes =[prime for prime in range(2,N+1) if all(prime%num != 0 for num in range(2,prime))]
        prime_factors = [prime_factor for prime_factor in all_primes if N%prime_factor == 0]
        return prime_factors

print(get_prime_factors(77))
print(get_prime_factors(0))
print(get_prime_factors(1))
print(get_prime_factors(1000001))
