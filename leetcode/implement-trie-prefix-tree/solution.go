// First solution (beats 67%)
type Trie struct {
    data map[byte]interface{}
}


func Constructor() Trie {
    return Trie{data: map[byte]interface{}{0: nil}}
}


func (this *Trie) Insert(word string)  {
    var node map[byte]interface{}
    node = this.data
    for i:=0;i<len(word);i++ {
        if _, ok := node[word[i]]; !ok {
            node[word[i]] = map[byte]interface{}{}
        }
        node = node[word[i]].(map[byte]interface{})
    }
    node[0] = nil
}


func (this *Trie) Search(word string) bool {
    if word == "" {
        return true
    }
    var node map[byte]interface{}
    node = this.data
    for i:=0;i<len(word);i++ {
        if _, ok := node[word[i]]; !ok {
            return false
        }
        node = node[word[i]].(map[byte]interface{})
    }
    if _, ok := node[0]; ok {
        return true
    }
    return false
}


func (this *Trie) StartsWith(prefix string) bool {
    if prefix == "" {
        return true
    }
    node := this.data
    for i:=0;i<len(prefix);i++ {
        if _, ok := node[prefix[i]]; !ok {
            return false
        }
        node = node[prefix[i]].(map[byte]interface{})
    }
    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */

// Seconds solution (beats 63%)
type Trie struct {
    data map[byte]*Trie
}


func Constructor() Trie {
    return Trie{data: map[byte]*Trie{}}
}


func (this *Trie) Insert(word string)  {
    if len(word) == 0 {
        this.data[0] = nil
        return
    }
    if _, ok := this.data[word[0]]; !ok {
        this.data[word[0]] = &Trie{data: map[byte]*Trie{}}
    }
    this.data[word[0]].Insert(word[1:])
    return
}


func (this *Trie) Search(word string) bool {
    if word == "" {
        if _, ok := this.data[0]; ok {
            return true
        } else {
            return false
        }
    }
    if val, ok := this.data[word[0]]; !ok {
        return false
    } else {
        return val.Search(word[1:])
    }
}


func (this *Trie) StartsWith(prefix string) bool {
    if prefix == "" {
        return true
    }
    if val, ok := this.data[prefix[0]]; !ok {
        return false
    } else {
        return val.StartsWith(prefix[1:])
    }
}

// Third solution (beats 60%)
type Trie struct {
    data map[byte]*Trie
}


func Constructor() Trie {
    return Trie{data: map[byte]*Trie{}}
}


func (this *Trie) Insert(word string)  {
    for i:=0;i<len(word);i++ {
        if _, ok := this.data[word[i]]; !ok {
            this.data[word[i]] = &Trie{data: map[byte]*Trie{}}
        }
        this = this.data[word[i]]
    }
    this.data[0] = nil
}


func (this *Trie) Search(word string) bool {
    for i:=0;i<len(word);i++ {
        if val, ok := this.data[word[i]]; !ok {
            return false
        } else {
            this = val
        }
    }
    if _, ok := this.data[0]; ok {
        return true
    } else {
        return false
    }
}


func (this *Trie) StartsWith(prefix string) bool {
    for i:=0;i<len(prefix);i++ {
        if val, ok := this.data[prefix[i]]; !ok {
            return false
        } else {
            this = val
        }
    }
    return true
}
