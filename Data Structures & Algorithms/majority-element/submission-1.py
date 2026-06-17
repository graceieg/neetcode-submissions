class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        newMap = {}

        for num in nums: 
            if num in newMap: 
                newMap[num] += 1
            else: 
                newMap[num] = 1
        return max(newMap, key=newMap.get)