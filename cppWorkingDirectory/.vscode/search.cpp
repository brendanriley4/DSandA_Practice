#include <iostream>
#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        int pivot = l;
        l = 0;
        r = nums.size() - 1;

        if (target <= nums[r] && target >= nums[pivot]) {
            l = pivot;
        } else {
            r = pivot - 1;
        }

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] > target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return -1;
    }
};


int main() {
    Solution solution;
    std::vector<int> nums = {1,3,5,6,7,8,9};
    int ans = solution.search(nums, 6);
    std::cout << ans << std::endl;
}