# First solution (beats 71%)
class Heap:
    def __init__(self, data):
        self.data = data
        self.l = len(data)

    def heap(self):
        for i in range((self.l-1)//2,-1,-1):
            self.heapify(i)

    def heapify(self, i):
        max_ = i
        l, r = 2*i+1, 2*i+2

        if l < self.l and self.data[l][0] > self.data[max_][0]:
            max_ = l
        if r < self.l and self.data[r][0] > self.data[max_][0]:
            max_ = r
        if max_ != i:
            self.data[i], self.data[max_] = self.data[max_], self.data[i]
            self.heapify(max_)

    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        ret = self.data[-1]
        self.l -= 1
        self.data = self.data[:self.l]
        self.heapify(0)
        return ret


class Twitter:

    def __init__(self):
        self.followers = defaultdict(dict)
        self.tweets = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = self.tweets[userId][:]
        for f in self.followers[userId]:
            h.extend(self.tweets[f])
        h = Heap(h)
        h.heap()
        ret = []
        i = 0
        while i < 10 and h.l >0:
            ret.append(h.pop()[1])
            i += 1

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].pop(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
