class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = True * n
        primes[0] = primes[1] = False
        """循环的范围进行了缩小"""
        for i in range(2, int(n ** 0.5) + 1):
            """先判断是否已经变为false，同时从i*i开始进行遍历"""
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)