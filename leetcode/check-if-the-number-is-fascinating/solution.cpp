class Solution {
public:
    bool isFascinating(int n) {
        int s[9] = {0};
        int i = 0;
        int k = 0;
        for (int j=0; j < 3; j++) {
            i = (j+1) * n;
            while (i > 0) {
                k = i % 10;
                if (k == 0) {
                    return false;
                }
                if (s[k-1] == k) {
                    return false;
                }
                s[k-1] = k;
                i = i / 10;
            }
        }
        return true;
    }
};
