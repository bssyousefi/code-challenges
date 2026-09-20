# First solution (beats 13%) (BFS)
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deads = set(deadends)
        forward = {str(i):str(i+1) for i in range(10)}
        forward['9'] = '0'
        backward = {str(i):str(i-1) for i in range(10)}
        backward['0'] = '9'

        q = deque()
        q.append((target, 0))
        visit = {target}
        while q:
            node ,step = q.popleft()
            if node == "0000":
                return step
            for map_ in [forward, backward]:
                for i in range(4):
                    new_node = node[:i] + map_[node[i]] + node[i+1:]
                    if new_node not in visit and new_node not in deadends:
                        visit.add(new_node)
                        q.append((new_node, step+1))

        return -1
