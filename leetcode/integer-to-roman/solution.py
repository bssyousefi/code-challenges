class Solution:
    m = {
        1: ["I", "V"],
        2: ["X", "L"],
        3: ["C", "D"],
        4: ["M"]
    }
    def intToRoman(self, num: int) -> str:
        ret = ''
        counter = 0
        while num > 0:
            counter += 1
            i = num % 10
            num = num // 10
            if i < 4:
                ret = i * self.m[counter][0] + ret
            elif i == 4:
                ret = self.m[counter][0] + self.m[counter][1] + ret
            elif i == 5:
                ret = self.m[counter][1] + ret
            elif i < 9:
                ret = self.m[counter][1] + (i-5) * self.m[counter][0] + ret
            elif i == 9:
                ret = self.m[counter][0] + self.m[counter+1][0] + ret

        return ret
