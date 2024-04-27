int lengthOfLongestSubstring(char* s) {
    if (!s || !*s)
        return 0;
    
    int cache[256];
    memset(cache, -1, sizeof(cache));

    int m = 0;
    int j = 0;
    int i = 0;

    for (i = 0; s[i] != '\0'; i++) {
        if ((cache[s[i]] != -1) && (cache[s[i]] >= j)) {
            m = (m > (i-j)) ? m : i-j;
            j = cache[s[i]] + 1;
        }
        cache[s[i]] = i;
    }
    return (m > (i-j)) ? m :i-j;
}
