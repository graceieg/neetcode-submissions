class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        curr = 0
        for num in range(len(nums) - k + 1):
            curr = heapq.heappop(nums)
        return curr
