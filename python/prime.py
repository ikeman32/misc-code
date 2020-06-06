def isPrime(n):
    if n <= 1:
        return False

    #Return True if number is 2,3,5 or 7
    if n <= 3 or n == 5 or n == 7:
        return True

    #List the first 4 prime numbers
    primes = [2, 3, 5, 7]

    #Loop through primes and perform modulo division
    #Return False if 0 otherwise Return True
    for i in primes:
        if n % i == 0:
            print(f'{n} is not a Prime number!')
            return False
        else:
            print(f'{n} is a Prime number!')
            return True

isPrime(int(input('Enter a number: ')))