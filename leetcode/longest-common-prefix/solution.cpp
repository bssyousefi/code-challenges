#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) {
            return "";
        }
        if (strs.size() == 1) {
            return strs[0];
        }
        int i = 0;
        int j = 1;
        char r;
        while (i <= strs[0].size()) {
            r = strs[0][i];
            for (j = 1; j < strs.size(); ++j) {
                if (i >= strs[j].size() || r != strs[j][i]) {
                    break;
                }
            }
            if (j != strs.size()) {
                i--;
                break;
            }
            i++;
        }
        return strs[0].substr(0,i+1);
    }
};
