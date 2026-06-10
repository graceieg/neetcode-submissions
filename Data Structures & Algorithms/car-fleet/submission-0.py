class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Car fleet = when cars are going the same mph

        #List position in miles
        #List speed in miles per hour

        #Target = miles

        # (Target - position_ / speed = iteration
        #if iteration == iteration then traveling at fleet 

        #Case = Fleet at Target 

        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p,s in sorted(pair)[::-1]:
            stack.append((target - p ) / s)
            if len(stack) > 1 and stack[-1] <= stack [-2]:
                stack.pop()
        return len(stack)
                                        
                


        