#First solution (beats 91%)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        sup = set(supplies)
        recps = {recipes[i]: i for i in range(len(recipes))}
        visit = [0] * len(recipes)
        ret = []

        def dfs(i):
            for ing in ingredients[i]:
                if ing not in sup:
                    if ing in recps:
                        if visit[recps[ing]] == 0:
                            visit[recps[ing]] = 1
                            if dfs(recps[ing]):
                                visit[recps[ing]] = 2
                            else:
                                visit[recps[ing]] = -1
                                return False
                        elif visit[recps[ing]] == -1:
                            return False
                        elif visit[recps[ing]] == 1:
                            return False
                    else:
                        return False
            return True

        for i in range(len(recipes)):
            if visit[i] != 0:
                continue
            visit[i] = 1
            if dfs(i):
                visit[i] = 2
            else:
                visit[i] = -1
        return [recipes[i] for i in range(len(recipes)) if visit[i] == 2]


