class Solution:
    def specialArray(self, nums: List[int]) -> int:
        #return x if there are x numbers greater or equal to x
        #return -1 if not 

        #array is non-negative
        #x doesnt have to be in nums
        #00344
        nums.sort()
        n = len(nums)
        i, j = 0, 1

        while i < n and j <= n:
            while i < n and j > nums[i]:
                i += 1

            if j == n - i:
                return j
            j += 1

        return -1