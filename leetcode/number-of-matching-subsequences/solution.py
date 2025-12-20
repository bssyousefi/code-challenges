# First solution (beats 8%) (95% memory)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        l = len(s)
        cache = {}
        def isSub(word):
            ll = len(word)
            if ll >= l:
                return False
            j = -1
            state = False
            for i in range(ll):
                state = False
                while j < l-1:
                    if word[i] == s[j+1]:
                        state = True
                        j += 1
                        break
                    j += 1

            return state

        counter = 0
        for word in words:
            if word not in cache:
                cache[word] = isSub(word)
            if cache[word]:
                counter += 1

        return counter

