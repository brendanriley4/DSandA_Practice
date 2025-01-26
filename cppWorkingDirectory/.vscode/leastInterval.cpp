#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {
        std::unordered_map <char, int> freq;

        // count frequencies of tasks
        for(auto& task : tasks) {
            freq[task]++;
        }

        // find max frequency
        int maxFreq = 0;
        for(auto& [task, count] : freq) {
            maxFreq = std::max(maxFreq, count);
        }

        // count the number of tasks with the highest frequency
        int maxFreqCount = 0;
        for(auto& [task, count] : freq) {
            if(count == maxFreq) {
                maxFreqCount++;
            }
        }

        // math equation: 
        int intervals = (maxFreq - 1) * (n - 1) + maxFreqCount;

        // compare to the number of tasks, we cannot have less intervals than tasks
        return std::max(intervals, (int)tasks.size());
    }
};

int main() {
    Solution solution;
    std::vector<char> tc = {'A', 'A', 'A', 'B', 'B', 'B'};
    int ans = solution.leastInterval(tc, 2);
    std::cout << ans << std::endl;
}