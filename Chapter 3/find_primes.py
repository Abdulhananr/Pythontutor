def sieve_of_eratosthenes(N):
    """
    Implement the Sieve of Eratosthenes algorithm to find all primes up to a given number.
    
    Parameters:
    N (int): The upper limit to find primes up to.
    
    Returns:
    list: A list of prime numbers up to N.
    """
    numbers = list(range(2, N + 1))
    primes = []
    for p in range(len(numbers)):
        if numbers[p] != 0:
            primes.append(numbers[p])
            for i in range(numbers[p], N + 1, numbers[p]):
                numbers[i - 2] = 0
    return primes

primes_up_to_100 = sieve_of_eratosthenes(100)
print(primes_up_to_100)

"""
Sample run:
python find_primes.py
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
