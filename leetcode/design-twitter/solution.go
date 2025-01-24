// First solution (beats 83%)
type Heap struct {
    data [][2]int
    l    int
}

func (h *Heap) heap() {
    for i:=(h.l-1)/2;i>-1;i-- {
        h.heapify(i)
    }
}

func (h *Heap) heapify(i int) {
    min_ := i
    l, r := 2*i+1, 2*i+2

    if l<h.l && h.data[l][0] < h.data[min_][0] {
        min_ = l
    }

    if r<h.l && h.data[r][0] < h.data[min_][0] {
        min_ = r
    }

    if min_ != i {
        h.data[i], h.data[min_] = h.data[min_], h.data[i]
        h.heapify(min_)
    }
}

func (h *Heap) push(v [2]int) {
    if h.l < 10 {
        h.data = append(h.data, v)
        h.l++
    } else {
        if h.data[0][0] < v[0] {
            h.data[0] = v
        }
    }
    h.heap()
}

func (h *Heap) pop() int {
    h.data[0], h.data[h.l-1] = h.data[h.l-1], h.data[0]
    ret := h.data[h.l-1][1]
    h.l--
    h.heapify(0)
    return ret
}

type Twitter struct {
    tweets    map[int][][2]int
    followers map[int][]int
    time      int
}


func Constructor() Twitter {
    return Twitter{
        tweets:  map[int][][2]int{},
        followers: map[int][]int{},
        time: 0,
    }
}


func (this *Twitter) PostTweet(userId int, tweetId int)  {
    if _, ok := this.tweets[userId]; !ok {
        this.tweets[userId] = make([][2]int,0,1)
    }
    this.tweets[userId] = append(this.tweets[userId], [2]int{this.time, tweetId})
    this.time++
}

func (this *Twitter) GetNewsFeed(userId int) []int {
    h := Heap{data: [][2]int{}}
    i := len(this.tweets[userId])-1
    count := 0
    for i >= 0 && count < 10 {
        h.push(this.tweets[userId][i])
        i--
        count++
    }
    for _, f := range this.followers[userId] {
        count = 0
        i = len(this.tweets[f])-1
        for i >= 0 && count < 10 {
            h.push(this.tweets[f][i])
            i--
            count++
        }
    }
    ret := make([]int, h.l)
    i = h.l-1
    for h.l > 0 {
        ret[i] = h.pop()
        i--
    }
    return ret
}


func (this *Twitter) Follow(followerId int, followeeId int)  {
    if _, ok := this.followers[followerId]; !ok {
        this.followers[followerId] = make([]int,0,1)
    }
    for _, v := range this.followers[followerId] {
            if v == followeeId {
                return
            }
        }
    this.followers[followerId] = append(this.followers[followerId], followeeId)
}


func (this *Twitter) Unfollow(followerId int, followeeId int)  {
    if _, ok := this.followers[followerId]; ok {
        for i, v := range this.followers[followerId] {
            if v == followeeId {
                this.followers[followerId] = append(this.followers[followerId][:i], this.followers[followerId][i+1:]...)
                break
            }
        }
    }
}


/**
 * Your Twitter object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PostTweet(userId,tweetId);
 * param_2 := obj.GetNewsFeed(userId);
 * obj.Follow(followerId,followeeId);
 * obj.Unfollow(followerId,followeeId);
 */
