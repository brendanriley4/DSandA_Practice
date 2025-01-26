#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1 || s.length() <= numRows) return s;

        vector<string> rows(min(numRows, int(s.length())));
        int currRow = 0;
        bool goingDown = false;

        for (char c : s) {
            rows[currRow] += c;
            if (currRow == 0 || currRow == numRows - 1) goingDown = !goingDown;
            currRow += goingDown ? 1 : -1;
        }

        string result;
        for (string row : rows) {
            result += row;
        }
        
        return result;
    }
};

int main() {
    Solution solution;
    string ans = solution.convert("PAYPALISHIRING", 3);
    cout << "Test case 1: " << ans << "\n";
}