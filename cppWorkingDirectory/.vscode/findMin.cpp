#include <vector>
#include <iostream>

class Solution {
public:
    int findMin(std::vector<int>& nums) {
        int r = nums.size() - 1;
        int l = 0;
        while(l < r) {
            int m = l + (r - l) / 2;
            if(nums[m] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return nums[l];
    }
};



int main() {
    Solution solution;
    // std::vector<int> tc = {3,4,5,1,2};
    std::vector<int> tc = {11,13,15,17};
    int ans = solution.findMin(tc);
    std::cout << ans << std::endl;
}