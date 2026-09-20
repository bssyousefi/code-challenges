# First solution (beats 100%)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [""]
        subs = path.split("/")
        for sub in subs:
            if sub == "":
                pass
            elif sub == "/":
                pass
            elif sub == ".":
                pass
            elif sub == "..":
                if stack[-1] != "":
                    stack.pop()
            else:
                stack.append(sub)

        if len(stack) <= 1:
            stack = ["", ""]

        return "/".join(stack)
