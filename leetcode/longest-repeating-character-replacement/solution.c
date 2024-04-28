int characterReplacement(char* s, int k) {
    int cache[256];
    memset(cache, 0, sizeof(cache));
    int i;
    int l = 0;
    int m = 0;

    for(i=0; s[i]!='\0'; i++) {
        cache[s[i]]++;
        m = m > cache[s[i]] ? m : cache[s[i]];

        if((i-l+1-m)>k) {
            cache[s[l]]--;
            l++;
        }
    }
    return i-l;
}
