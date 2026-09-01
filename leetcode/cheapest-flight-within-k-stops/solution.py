# First solution (Time out) (BFS with priority queue)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        routes = defaultdict(list)
        flights.sort(key=lambda x:x[2])
        for source, dest, price in flights:
            routes[source].append((price, dest))
        q = [(0,0,src, set())]
        while q:
            cost, n, city, cache = heapq.heappop(q)
            if n >= k+1 and city != dst:
                continue
            if city == dst:
                return cost
                continue
            cache.add(city)
            for price, dest in routes[city]:
                if dest not in cache:
                    heapq.heappush(q, (cost+price,n+1, dest, {*cache}))
        return -1

# Second solution (beats 5%) (BFS with priority queue and better cache)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        routes = defaultdict(list)
        flights.sort(key=lambda x:x[2])
        for source, dest, price in flights:
            routes[source].append((price, dest))
        q = [(0,0,src)]
        cache = defaultdict(lambda : 2*k)
        while q:
            cost, n, city = heapq.heappop(q)
            if n >= k+1 and city != dst:
                continue
            if city == dst:
                return cost

            cache[city] = n
            for price, dest in routes[city]:
                if cache[dest] >= n:
                    heapq.heappush(q, (cost+price,n+1, dest))
        return -1

