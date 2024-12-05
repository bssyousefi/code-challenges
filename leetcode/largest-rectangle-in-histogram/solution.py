# First solution (beats 6%) (beats 80% in memory)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        i = 0
        heights.append(0)
        while i < len(heights):
            if len(stack) > 0 and heights[i] < stack[-1][1]:
                j = 0
                while j < len(stack):
                    if j == 0:
                        area = max(area, stack[0][1] * (i))
                    else:
                        area = max(area, stack[j][1] * (i - 1 - stack[j-1][0]))
                    j += 1
            while i < len(heights)-1 and heights[i] == heights[i+1]:
                i += 1
            while len(stack) > 0 and  heights[i] <= stack[-1][1]:
                j, _ = stack.pop()

            stack.append((i, heights[i]))
            i += 1
        return area

# Second solution (beats 12%) (Remove extra blocks)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        i = 0
        heights.append(0)
        while i < len(heights):
            while len(stack) > 0 and  heights[i] < stack[-1][1]:
                j, v = stack.pop()
                if len(stack) == 0:
                    area = max(area, v * i)
                else:
                    area = max(area, v * (i - 1 - stack[-1][0]))

            stack.append((i, heights[i]))
            i += 1
        return area

# Third solution (beats 47%)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [-1]
        i = 0
        heights.append(0)
        while i < len(heights):
            while heights[i] < heights[stack[-1]]:
                j = stack.pop()
                area = max(area, heights[j] * (i - 1 - stack[-1]))

            stack.append(i)
            i += 1
        return area

# Fourth solution (beats 87%) (change while with for??)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [-1]
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                j = stack.pop()
                area = max(area, heights[j] * (i - 1 - stack[-1]))

            stack.append(i)
            i += 1
        return area
