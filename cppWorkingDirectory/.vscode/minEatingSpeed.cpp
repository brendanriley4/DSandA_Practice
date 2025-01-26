#include <vector>
#include <iostream>
#include <algorithm>

class Solution {
public:
    int minEatingSpeed(std::vector<int>& piles, int h) {
        int high = *std::max_element(piles.begin(), piles.end());
        int low = 1;
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int currTime = h;
            for (int pile : piles) {
                currTime -= (pile + mid - 1) / mid;
            }
            if (currTime >= 0) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};

int main () {
    Solution solution;
    std::vector<int> tc = {30,11,23,4,20};
    int ans = solution.minEatingSpeed(tc, 6);
    std::cout << ans << std::endl;
}