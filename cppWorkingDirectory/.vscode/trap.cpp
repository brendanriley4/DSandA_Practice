#include <vector>
#include <algorithm>
#include <iostream>

class Solution {
public:
    int trap(std::vector<int>& height) {
        if(height.size() == 1) {
            return 0;
        }
        int area = 0;
        std::vector<int> left(height.size());
        std::vector<int> right(height.size());
        fill(left.begin(), left.end(), 0);
        fill(right.begin(), right.end(), 0);
        int i = 0;
        int max = 0;
        while(i < left.size()) {
            left[i] = max;
            if(height[i] > max) {
                max = height[i];
            }
            i++;
        }
        i = right.size() - 1;
        max = 0;
        while(i > 0) {
            right[i] = max;
            if(height[i] > max) {
                max = height[i];
            }
            i--;
        }
        i = 1;
        while(i < height.size() - 1) {
            area = area + std::max((std::min(left[i], right[i]) - height[i]), 0);
            i++;
        }
        return area;
    }
};

int main() {
    Solution solution;

    std::vector<int> tc = {4,2,0,3,2,5};

    // std::vector<int> tc = {0,1,0,2,1,0,1,3,2,1,2,1};
    int ans = solution.trap(tc);
    std::cout << ans << std::endl;
}