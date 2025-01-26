#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> row(n, 1);
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                row[j] = row[j] + row[j + 1];
            }
        }
        return row[0];        
    }
};

int main() {
    Solution solution;
    int ans = solution.uniquePaths(3, 7);
    cout << "Test case 1: " << ans << "\n";
}