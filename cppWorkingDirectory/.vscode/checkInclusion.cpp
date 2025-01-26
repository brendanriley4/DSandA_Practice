#include <string>
#include <iostream>
#include <vector>

class Solution {
public:
    bool checkInclusion(std::string s1, std::string s2) {
        if (s1.length() > s2.length()) return false;

        std::vector<int> freq1(26, 0), freq2(26, 0);
        int match_count = 0;

        for (int i = 0; i < s1.length(); i++) {
            freq1[s1[i] - 'a']++; 
            freq2[s2[i] - 'a']++; 
        }

        for (int i = 0; i < 26; i++) {
            if (freq1[i] == freq2[i]) match_count++;
        }

        for (int i = s1.length(); i < s2.length(); i++) {
            if (match_count == 26) return true;
    
            char in_char = s2[i];
            char out_char = s2[i - s1.length()];

            freq2[in_char - 'a']++;

            if (freq2[in_char - 'a'] == freq1[in_char - 'a']) match_count++;
            else if (freq2[in_char - 'a'] - 1 == freq1[in_char - 'a']) match_count--;

            freq2[out_char - 'a']--;

            if (freq2[out_char - 'a'] == freq1[out_char - 'a']) match_count++;
            else if (freq2[out_char - 'a'] + 1 == freq1[out_char - 'a']) match_count--;
        }

        return match_count == 26;
    }
};


int main () {
    Solution solution;
    std::string s1 = "hello";
    std::string s2 = "ooolleoooleh";
    bool ans = solution.checkInclusion(s1,s2);
    std::cout << ans << std::endl;
}