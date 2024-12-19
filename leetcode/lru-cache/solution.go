// First solution (beats 85%) (based on lru-cache implementation in Cpython)
type Node struct {
    pre *Node
    nex *Node
    key int
    value int
}

type LRUCache struct {
    cache map[int]*Node
    root *Node
    cap int
}


func Constructor(capacity int) LRUCache {
    root := &Node{}
    root.pre, root.nex = root, root
    return LRUCache{make(map[int]*Node), root, capacity}
}


func (this *LRUCache) Get(key int) int {
    if v, ok := this.cache[key]; ok {
        v.pre.nex, v.nex.pre = v.nex, v.pre
        v.pre, v.nex = this.root, this.root.nex
        this.root.nex.pre = v
        this.root.nex = v
        return v.value
    } else {
        return -1
    }
}


func (this *LRUCache) Put(key int, value int)  {
    if v, ok := this.cache[key]; ok {
        v.pre.nex, v.nex.pre = v.nex, v.pre
        v.pre, v.nex = this.root, this.root.nex
        this.root.nex.pre = v
        this.root.nex = v
        v.value = value
    } else {
        if len(this.cache) == this.cap {
            delete(this.cache, this.root.pre.key)
            this.root.pre.pre.nex = this.root
            this.root.pre = this.root.pre.pre
        }
        node := &Node{this.root, this.root.nex, key, value}
        this.root.nex.pre = node
        this.root.nex = node
        this.cache[key] = node
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
