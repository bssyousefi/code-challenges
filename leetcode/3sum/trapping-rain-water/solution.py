# First solution (beats 55%) (horizontal calculation)
class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        mem = [(0, height[0])]
        for i in range(1, len(height)):
            if height[i] < mem[-1][1]:
                mem.append((i, height[i]))
            else:
                while len(mem) > 0 and height[i] > mem[-1][1]:
                    j, v = mem.pop()
                    if len(mem) > 0:
                        area += (i - mem[-1][0]-1) * (min(height[i], mem[-1][1]) - v)
                else:
                    mem.append((i, height[i]))

        return area
# Second solution (beats 90%) (vertical calculation)
class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        while (l < r):
            if height[l] < height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    area += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    area += rmax - height[r]
                r -= 1

        return area
