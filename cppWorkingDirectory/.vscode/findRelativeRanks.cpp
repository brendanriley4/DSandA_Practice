#include <vector>
#include <string>
#include <iostream>
#include <queue>
#include <unordered_map>
using namespace std;


class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        priority_queue<pair<int, int>> max_heap;
        vector<string> ret(score.size());
        for(int i = 0; i < score.size(); i++) {
            max_heap.push({score[i], i});
        }
        int i = 0;
        while(!max_heap.empty()) {
            auto max = max_heap.top();
            if(i == 0) {
                ret[max.second] = "Gold Medal";
                i += 1;
            }
            else if(i == 1) {
                ret[max.second] = "Silver Medal";
                i += 1;
            }
            else if(i == 2) {
                ret[max.second] = "Bronze Medal";
                i += 1;
            } else {
                ret[max.second] = to_string(i + 1);
                i += 1;
            }         
            max_heap.pop();   
        }
        return ret;
    }
};


void main() {
    Solution solution;

    vector<int> tc = {5, 4, 3, 2, 1};
    vector<string> ans = solution.findRelativeRanks(tc);
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << ", ";
    }
}