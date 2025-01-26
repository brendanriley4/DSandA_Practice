#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m  = obstacleGrid.size();
        int n = m > 0 ? obstacleGrid[0].size(): 0;
        if(obstacleGrid[m - 1][n - 1] == 1 || obstacleGrid[0][0] == 1 || m == 0 || n == 0) {
            return 0;
        }
        vector<int> row(n, 0);
        row[n - 1] = obstacleGrid[m - 1][n - 1] == 0 ? 1 : 0;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if(obstacleGrid[i][j] == 1) {
                    row[j] = 0;
                }
                else if(j < n - 1) {
                    row[j] = row[j] + row[j + 1];
                }
            }
        }
        return row[0];
    }
};

int main() {
    Solution solution;
    // vector<vector<int>> testCase = {{0,1},{0,0}};
    // int ans = solution.uniquePathsWithObstacles(testCase);
    // cout << "Test case1: " << ans;

    // cout << "\n";

    vector<vector<int>> testCase2 = {{0,0,0},{0,1,0},{0,0,0}};
    int ans2 = solution.uniquePathsWithObstacles(testCase2);
    cout << "Test case2: " << ans2;
}