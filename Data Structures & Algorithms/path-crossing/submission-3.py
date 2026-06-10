class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        x = 0
        y = 0
        seen.add((0,0))
     
        for i in range(len(path)):
            
            if path[i] == 'N':
                y += 1
                if ((x,y)) not in seen: 
                    seen.add((x,y))
                else: 
                    return True

            elif path[i] == 'S':
                y -= 1
                if ((x,y)) not in seen: 
                    seen.add((x,y))
                else: 
                    return True

            elif path[i] == 'E':
                x += 1
                if ((x,y)) not in seen: 
                    seen.add((x,y))
                else: 
                    return True

            elif path[i] == 'W': 
                x -= 1
                if ((x,y)) not in seen: 
                    seen.add((x,y))
                else: 
                    return True
        
        return False
