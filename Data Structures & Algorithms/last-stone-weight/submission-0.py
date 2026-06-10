class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x,y = 0,0
    
        while len(stones) > 1: 
            stones.sort()
            x = stones.pop()
            y = stones.pop()

            if x < y: 
                y = y - x
                stones.append(y)
            elif x > y:
                x = x-y
                stones.append(x)
        if stones: 
            return stones[0]
        else: 
            return 0

        

        

        