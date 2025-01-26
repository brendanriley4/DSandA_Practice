#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> myMap;
        unordered_map<string, char> myMap2;
        istringstream iss(s);
        string word;
        vector<string> words;

        while (iss >> word) {
            words.push_back(word);
        }

        if (words.size() != pattern.size()) return false;

        for (size_t i = 0; i < pattern.size(); i++) {
            char c = pattern[i];

            if (myMap.count(c)) {
                if (myMap[c] != words[i]) return false;
            }
            else {
                if (myMap2.count(words[i])) {
                    if (myMap2[words[i]] != c) return false; 
                }

                myMap[c] = words[i];
                myMap2[words[i]] = c;
            }
        }
        return true;
    }
};

int main() {
    Solution solution;
    bool ans = solution.wordPattern("abba", "dog cat cat dog");
    cout << "Test case 1: " << ans << "\n";
}