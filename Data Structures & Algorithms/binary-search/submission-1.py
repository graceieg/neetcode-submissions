class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = 0
        res = -1
        while l <= r: 
            mid = (r + l) // 2
            if nums[mid] == target: 
                res = mid
                return res
            if nums[mid] > target: 
                r -= 1
            else: 
                l += 1
        return res
        
        