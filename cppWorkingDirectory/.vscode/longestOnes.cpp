#include <vector>
#include <iostream>
#include <algorithm>

class Solution {
public:
    int longestOnes(std::vector<int>& nums, int k) {
        int l = 0;
        int r = 0;
        int max = 0;
        while (r < nums.size()) {
            if (nums[r] == 0) {
                k--;
            }
            while (k < 0) {
                if (nums[l] == 0) {
                    k++;
                }
                l++;
            }
            
            max = std::max(max, r - l + 1);
            r++;
        }
        return max;
    }
};

int main () {
    Solution solution;
    std::vector<int> nums = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
    int k = 3;
    int ans = solution.longestOnes(nums, k);
    std::cout << ans << std::endl;
}
