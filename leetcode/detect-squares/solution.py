# First solution (beats 92%)
class DetectSquares:

    def __init__(self):
        self.rows = defaultdict(lambda:defaultdict(int))
        self.cols = defaultdict(lambda:defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.rows[point[1]][point[0]] += 1
        self.cols[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for i in self.cols[x]:
            if i != y:
                d = abs(i-y)
                if (k:=self.rows[i][x+d]) and (l:=self.cols[x+d][y]):
                    count += k*l*self.cols[x][i]
                if (k:=self.rows[i][x-d]) and (l:=self.cols[x-d][y]):
                    count += k*l*self.cols[x][i]
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
