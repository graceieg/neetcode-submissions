class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites: 
            crsMap[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit: 
                return False

            if crsMap[crs] == []:
                return True
            visit.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre): 
                    return False
            visit.remove(crs)
            crsMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c): 
                return False
        return True