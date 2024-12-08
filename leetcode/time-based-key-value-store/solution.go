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

// Second solution (beats 99%)
type TimeMap struct {
    key map[string]*Key
}

type Key struct {
    data []string
    time []int
}


func Constructor() TimeMap {
    return TimeMap{make(map[string]*Key)}
}

func (this *TimeMap) Set(key string, value string, timestamp int)  {
    if v, ok := this.key[key]; ok {
        v.data = append(v.data, value)
        v.time = append(v.time, timestamp)
    } else {
        this.key[key] = &Key{[]string{value}, []int{timestamp}}
    }
}

func (this *TimeMap) Get(key string, timestamp int) string {
    if v, ok := this.key[key]; ok {
        i, j := 0, len(v.data) - 1
        for i <= j {
            m := (i + j) / 2
            if v.time[m] > timestamp {
                j = m - 1
            } else {
                i = m + 1
            }
        }
        if j >= 0 {
            return v.data[j]
        } else {
            return ""
        }
    } else {
        return ""
    }
}
