type TimeMap struct {
    times map[string][]int
    values map[string][]string
}


func Constructor() TimeMap {
    t := TimeMap{
        times : make(map[string][]int),
        values : make(map[string][]string),
    }
    return t
}


func (this *TimeMap) Set(key string, value string, timestamp int)  {
    _, ok := this.times[key]
    if !ok {
      this.times[key] = make([]int, 1)
      this.values[key] = make([]string, 1)  
    } 
    this.times[key] = append(this.times[key], timestamp)
    this.values[key] = append(this.values[key], value)
}


func (this *TimeMap) Get(key string, timestamp int) string {
    v, ok := this.times[key]
    if !ok {
        return ""
    } else {
        l := 0
        r := len(v) - 1
        for l<=r {
            m := (l+r) / 2
            if v[m] == timestamp {
                return this.values[key][m]
            } else if v[m] < timestamp {
                l = m + 1
            } else {
                r = m - 1
            }
        }
        return this.values[key][r]
    }
}


/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
