bool checkInclusion(char* s1, char* s2) {
    int m[26];
    int n[26];
    memset(m, 0, sizeof(m));
    memset(n, 0, sizeof(n));

    int i,j;
    int l=0;

    for(i=0;s1[i]!='\0';i++) {
        if(s2[i]=='\0') {
            return 0;
        }
        m[s1[i]-'a']++;
        n[s2[i]-'a']++;
    }
    for(j=0;j<26;j++) {
        if(m[j] == n[j]) {
            l++;
        }
    }

    if(l==26) {
        return 1;
    }
    j = 1;
    for(;s2[i]!='\0';i++, j++) {
        if(n[s2[j-1]-'a'] == m[s2[j-1]-'a']) {
            l--;
        }
        n[s2[j-1]-'a']--;
        if(n[s2[j-1]-'a'] == m[s2[j-1]-'a']) {
            l++;
        }
        if(n[s2[i]-'a'] == m[s2[i]-'a']) {
            l--;
        }
        n[s2[i]-'a']++;
        if(n[s2[i]-'a'] == m[s2[i]-'a']) {
            l++;
        }
        if(l==26) {
            return 1;
        }
    }
    if(l==26) {
        return 1;
    }
    return 0;
}
