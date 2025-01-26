#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;

        int n = intervals.size();
        int i = 0;

        // Add all intervals before the new interval
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }

        // Merge all overlapping intervals with the new interval
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.push_back(newInterval);

        // Add all intervals after the new interval
        while (i < n) {
            result.push_back(intervals[i]);
            i++;
        }

        return result;
    }
};

// const - makes interval constant value, can't accidentally screw with it
// & - makes interval reference the memory of it's input and not create a copy
// auto - allows compiler to deduce the type of data based off of what is passed in (what type is vec) 
void printVector(const vector<vector<int>>& vec) { 
    for (const auto& interval : vec) {
        cout << "[" << interval[0] << ", " << interval[1] << "] ";
    }
    cout << endl;
}

int main() {
    Solution solution;
    vector<vector<int>> myList = {{1,3},{6,9}};
    vector<int> myList2 = {2,5};
    vector<vector<int>> ans = solution.insert(myList, myList2);
    cout << "Test case 1: \n";
    printVector(ans);
}