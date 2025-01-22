# First solution (beats 11%) (DFS)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        visit = set()
        cache = {}
        ret = []
        def cal(i,j, k):
            state = False
            if i < 0 or j < 0:
                return 1
            if i == rows or j == cols:
                return 2

            if k != -1 and k < heights[i][j]:
                return 0
            elif k == heights[i][j]:
                state = True
            if (i,j) in cache:
                return cache[(i,j)]
            ret = 0
            visit.add((i,j))
            for r, c in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                if (r,c) in visit:
                    continue
                v = cal(r, c, heights[i][j])
                if v >= 3 or ret >= 3:
                    ret = 3
                    break
                elif v != ret:
                    ret += v
            visit.remove((i,j))
            if not state or ret == 3:
                cache[(i,j)] = ret
            return ret

        for i in range(rows):
            for j in range(cols):
                if cal(i,j,-1) == 3:
                    ret.append([i,j])
        return ret
# Second solution (beats 91%) (DFS, flow upward from boundaries)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        visitP = set()
        visitA = set()
        dx = [(-1,0),(0,-1),(1,0),(0,1),]
        ret = []
        def flowUp(i,j, v):
            v.add((i,j))
            for dr,dc in dx:
                ii, jj = i+dr, j+dc
                if ii < 0 or jj < 0 or ii == rows or jj == cols or ((ii,jj) in v) or heights[ii][jj] < heights[i][j]:
                    continue
                flowUp(ii,jj,v)

        for i in range(rows):
            flowUp(i,0,visitP)
            flowUp(i,cols-1,visitA)

        for j in range(cols):
            flowUp(0,j,visitP)
            flowUp(rows-1,j,visitA)

        for i, j in visitP:
            if (i,j) in visitA:
                ret.append([i,j])

        return ret
