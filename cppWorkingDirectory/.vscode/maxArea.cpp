#include <vector>
#include <iostream>
#include <algorithm>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int ans = 0;
        int left = 0;
        int right = height.size() - 1;
        while(left < right) {
            int area = (right - left) * std::min(height[left], height[right]);
            ans = std::max(ans, area);
            if(height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;

    std::vector<int> tc = {1,8,6,2,5,4,8,3,7};
    int ans = solution.maxArea(tc);
    std::cout << ans << std::endl;
}