#include <string>
#include <iostream>
#include <set>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int ans = 0;
        int l = 0;
        int r = 0;
        std::set<char> mySet;
        while (r < s.length()) {
            if (mySet.find(s[r]) != mySet.end()) {
                while (s[l] != s[r]) {
                    mySet.erase(s[l]);
                    l++;
                }
                l++;
            } else {
                mySet.insert(s[r]);
            }
            ans = std::max(ans, r - l + 1);
            r++;
        }
        return ans;
    }
};


int main () {
    Solution solution;
    std::string s = "abcabcbb";
    int ans = solution.lengthOfLongestSubstring(s);
    std::cout << ans << std::endl;
}