#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        int ans = 0;
        
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int> & a, const std::vector<int>& b) {
            return a[1] < b[1];
        });

        int end = intervals[0][1];

        for(int i = 1; i < intervals.size(); i++) {
            if(intervals[i][0] < end) {
                ans++;
            } else { 
                end = intervals[i][1];
            }  
        }       

        return ans; 
    }
};

int main() {
    Solution solution;
    std::vector<std::vector<int>> tc = {{1,2},{2,3},{3,4},{1,3}};
    int ans = solution.eraseOverlapIntervals(tc);
    std::cout << ans << std::endl;
}