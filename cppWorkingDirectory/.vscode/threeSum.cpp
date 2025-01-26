#include <vector>
#include <iostream>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> ans;
        std::sort(nums.begin(), nums.end());
        int previ = 1;
        for(int i = 0; i < nums.size() - 2; i++) {
            if(previ == nums[i]) {
                continue;
            }
            int oneSum = -nums[i];
            int high = nums.size() - 1;
            int low = i + 1;
            while(low < high) {
                int sum = nums[low] + nums[high];
                if(sum == oneSum) {
                    ans.push_back({nums[i], nums[low], nums[high]});
                    while(low < high && nums[low] == nums[low + 1]) {
                        low = low + 1;
                    }
                    while(low < high && nums[high] == nums[high - 1]) {
                        high = high - 1;
                    }
                    low = low + 1;
                    high = high - 1;
                } else if(sum < oneSum) {
                    low = low + 1;
                } else {
                    high = high - 1;
                }
            }
            previ = nums[i];
        }
        return ans;
    }
};


int main () {
    Solution solution;
    std::vector<int> tc = {0,0,0};
    std::vector<std::vector<int>> ans = solution.threeSum(tc);
    for(int i = 0; i < ans.size(); i++) {
        for(int j = 0; j < ans[0].size(); j++) {
            std::cout << ans[i][j];
        }
        std::cout << std::endl;
    }
}