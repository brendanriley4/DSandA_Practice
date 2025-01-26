#include <string>
#include <iostream>

class Solution {
public:
    int convertTime(std::string current, std::string correct) {
        int current_min = std::stoi(current.substr(3,2));
        int current_hour = std::stoi(current.substr(0,2));
        int correct_min = std::stoi(correct.substr(3,2));
        int correct_min = std::stoi(current.substr(0,2));
        if (current_min < correct_min) {
            
        }
    }
};

int main () {
    Solution solution;
    std::string tc = "02:30";
    std::string tc2 = "02:35";
    int ans = solution.convertTime(tc, tc2);
    std::cout << ans << std::endl;
}