class Solution: 
    def climbStairs(self, n: int): 
        memo = {}

        def dp(stair):
            if stair in memo:
                return memo[stair]

            if stair == 1: 
                return 1
            if stair == 2: 
                return 2

            memo[stair] = dp(stair -1) + dp(stair - 2)

            return dp(stair -1) + dp(stair - 2)


        return dp(n)

        