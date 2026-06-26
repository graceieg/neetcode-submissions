class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # store the least coins min in memo array
        # for each type of coin we dp if amount % coin not available in array
        # return -1
        #return dp(i)

        memo = {}

        def dfs(amount):
            if amount == 0: 
                return 0

            if amount in memo: 
                return memo[amount]

            res = 1e9
            for coin in coins: 
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount-coin))
            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins