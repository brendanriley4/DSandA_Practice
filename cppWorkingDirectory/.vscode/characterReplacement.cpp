#include <string>
#include <iostream>
#include <unordered_map>

class Solution {
public:
    int characterReplacement(std::string s, int k) {
        int l = 0;
        int r = 0;
        int max_length = 0;
        int max_freq = 0;
        std::unordered_map<char, int> freq; 
        while (r < s.length()) {
            freq[s[r]]++;
            max_freq = (max_freq > freq[s[r]]) ? max_freq : freq[s[r]];
            while (max_freq + k < (r - l+ 1)) {
                freq[s[l]]--;
                l++;
            }
            max_length = (max_length < (r - l + 1)) ? (r - l + 1) : max_length;
            r++;
        }
        return max_length;
    }
};

int main () {
    std::string s = "AABABBA";
    int k = 1;
    Solution solution;
    int ans = solution.characterReplacement(s, k);
    std::cout << ans << std::endl;
}