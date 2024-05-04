func minWindow(s string, t string) string {
	m := make(map[byte]int)
	n := make(map[byte]int)
	for i := 0; i < len(t); i++ {
		m[t[i]] = m[t[i]] + 1
	}
	l := 0
	r := 0
	matches := 0
	k := 1 << 16
	res := -1

	for r < len(s) {
		if m[s[r]] > 0 {
			n[s[r]] += 1
			if n[s[r]] <= m[s[r]] {
				matches += 1
			}
		}

		for matches == len(t) {
			if k > r-l+1 {
				k = r - l + 1
				res = l
			}
			if m[s[l]] > 0 {
				n[s[l]] -= 1
				if n[s[l]] < m[s[l]] {
					matches -= 1
				}
			}
			l += 1
		}
		r += 1
	}
    if res == -1 {
		return ""
	} else {
		return s[res : res+k]
	}
}
