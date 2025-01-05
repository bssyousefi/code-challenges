// First solution (beats 51%)
type WordDictionary struct {
    children map[byte]*WordDictionary
    end      bool
}


func Constructor() WordDictionary {
    return WordDictionary{children: map[byte]*WordDictionary{}}
}


func (this *WordDictionary) AddWord(word string)  {
    for i:=0;i<len(word);i++ {
        if _, ok := this.children[word[i]]; !ok {
            this.children[word[i]] = &WordDictionary{children: map[byte]*WordDictionary{}}
        }
        this = this.children[word[i]]
    }
    this.end = true
}


func (this *WordDictionary) Search(word string) bool {
    if word == "" {
        return this.end
    }
    if word[0] != '.' {
        if val, ok := this.children[word[0]]; ok {
            return val.Search(word[1:])
        } else {
            return false
        }
    } else {
        for _, child := range this.children {
            if child.Search(word[1:]) {
                return true
            }
        }
        return false
    }
}
// Second solution (beats 92%) (used more memory)
type WordDictionary struct {
    children [26]*WordDictionary
    end      bool
}


func Constructor() WordDictionary {
    return WordDictionary{}
}


func (this *WordDictionary) AddWord(word string)  {
    for i:=0;i<len(word);i++ {
        c := word[i] - 'a'
        if this.children[c] == nil {
            this.children[c] = &WordDictionary{}
        }
        this = this.children[c]
    }
    this.end = true
}


func (this *WordDictionary) Search(word string) bool {
    if word == "" {
        return this.end
    }
    if word[0] != '.' {
        c := word[0] - 'a'
        if this.children[c] != nil {
            return this.children[c].Search(word[1:])
        } else {
            return false
        }
    } else {
        for _, child := range this.children {
            if child != nil && child.Search(word[1:]) {
                return true
            }
        }
        return false
    }
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
