class Solution:
    def isArmstrong(self, n: int) -> bool:
        def getSumOfKthPowerOfDigits(num, k):
            result = 0

            while num != 0:
                result += (num % 10) ** k
                num //= 10

            return result

        length = len(str(n))

        return getSumOfKthPowerOfDigits(n, length) == n