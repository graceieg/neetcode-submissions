class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Calculates x ^ n

        #For loop in range n where prod *= x
        #return foat

        prod = 1 
        i = 0

        if n > 0: 
            while i < n:
                prod *= x
                i += 1
            return float(prod)
        else: 
            while i < abs(n):
                prod *= x
                i += 1
            return 1/(float(prod))
