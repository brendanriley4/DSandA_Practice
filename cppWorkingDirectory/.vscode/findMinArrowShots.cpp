#include <vector>
#include <iostream>
#include <algorithm>

class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        int n = points.size();

        std::sort(points.begin(), points.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] < b[0];
        });

        int end = points[0][1];

        for(int i = 1; i < points.size(); i++) {
            if(points[i][0] <= end) {
                n--;
                end = std::min(points[i][1], end);
            } else {
                end = points[i][1];
            }
        }
        return n;
    }
};

int main() {
    Solution solution;
    std::vector<std::vector<int>> tc = {{10,16},{2,8},{1,6},{7,12}};
    int ans = solution.findMinArrowShots(tc);
    std::cout << ans << std::endl;
}