class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mList = [element for row in matrix for element in row]
        l, r = 0, len(mList) - 1
        mid = 0

        while l <= r:
            mid = (l + r) // 2
            if mList[mid] == target:
                return True
            if mList[mid] > target:
                r -= 1
            if mList[mid] < target:
                l += 1
        return False
                



        

