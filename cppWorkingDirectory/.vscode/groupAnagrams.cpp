#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        
        // This creates a list of  

        std::unordered_map<std::string, std::vector<std::string>> groups;
        for (const auto& str : strs) {
            std::string sortedStr = str;
            std::sort(sortedStr.begin(), sortedStr.end());
            groups[sortedStr].push_back(str);
        }
        std::vector<std::vector<std::string>> ans;
        for (const auto& group : groups) {
            ans.push_back(group.second);
        }
        return ans;
        
        
        
        
        
        
        // std::vector<std::vector<std::string>> ans;
        // for(int i = 0; i < strs.size(); i++) {
        //     std::map<char, int> myMap;
        //     for(char letter : strs[i]) {
        //         if(myMap[letter]) {
        //             myMap[letter] += 1;
        //         } else {
        //             myMap[letter] = 1;
        //         }
        //     }
        //     std::vector<std::string> curr;
        //     curr.push_back({strs[i]});
        //     for (int j = i + 1; j < strs.size(); j++) {
        //         if(strs[j].size() != strs[i].size()) {
        //             continue;
        //         }
        //         std::map<char, int> newMap = myMap;
        //         bool add = true;
        //         for(int k = 0; k < strs[j].size(); k++) {
        //             if(!newMap[strs[j][k]] || newMap[strs[j][k]] == 0) {
        //                 add = false;
        //                 break;
        //             }
        //             newMap[strs[j][k]] -= 1;
        //         }
        //         if(add){
        //             curr.push_back({strs[j]});
        //             strs.erase(strs.begin() + j);
        //         }
        //     }
        //     if(!curr.empty()) {
        //         ans.push_back(curr);
        //     }
        // }
        // return ans;
    }
};


int main() {
    Solution solution;
    std::vector<std::string> tc = {"eat","tea","tan","ate","nat","bat"};
    std::vector<std::vector<std::string>> ans = solution.groupAnagrams(tc);
    for(int i = 0; i < ans.size(); i++) {
        for(int j = 0; j < ans[0].size(); j++) {
            std::cout << ans[i][j];
        }
        std::cout << std::endl;
    }
    
    std::vector<std::string> tc2 = {"","",""};
    std::vector<std::vector<std::string>> ans2 = solution.groupAnagrams(tc2);
    for(int i = 0; i < ans2.size(); i++) {
        for(int j = 0; j < ans2[0].size(); j++) {
            std::cout << ans2[i][j];
        }
        std::cout << std::endl;
    }
}