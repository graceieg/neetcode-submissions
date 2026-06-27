class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = defaultdict(int)
        res = []
        for num in nums: 
            frequencyMap[num] += 1
        
        frequencyMap = dict(sorted(frequencyMap.items(), key=lambda item:item[1], reverse= True)[:k])

        return list(frequencyMap)