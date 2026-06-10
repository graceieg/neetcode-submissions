class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0, 1
        looking = 0
        result = []
        for i in range(len(nums)): 
            looking = target - nums[i]
            if looking in nums and nums.index(looking) != i:
                result.append(min(i,nums.index(looking)))
                result.append(max(i,nums.index(looking)))
                return result

