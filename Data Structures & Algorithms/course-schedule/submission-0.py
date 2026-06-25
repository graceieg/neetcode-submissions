class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preMap[crs].append(prq)
        #visitSet
        visit = set()
        def dfs(crs):
            if crs in visit: 
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for prq in preMap[crs]:
                if not dfs(prq): return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True 
