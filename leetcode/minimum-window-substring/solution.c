char* minWindow(char* s, char* t) {
    int m[255] = {0};
    int n[255] = {0};
    int matches = 0;
    int k = 1<<15;
    int res = -1;
    for(int i=0;t[i] != '\0';i++) {
        m[t[i]]++;
        matches++;
    }
    int l = 0;
    int r = 0;
    while(s[r]!='\0'){
        n[s[r]]++;
        if(n[s[r]] <= m[s[r]]) {
            matches--;
        }
        while((matches == 0) && (l<=r)) {
            if(k > (r-l+1)) {
                k = r-l+1;
                res = l;
            }
            n[s[l]]--;
            if(n[s[l]] < m[s[l]]) {
                matches++;
            }
            l++;
        }
        r++;
    }
    char *ret = malloc((k+1)*sizeof(char));
    
    if(res!=-1){
        strncpy(ret,s+res,k);
        ret[k] = '\0';
    } else {
        ret[0] = '\0';
    }
    return ret;
}
