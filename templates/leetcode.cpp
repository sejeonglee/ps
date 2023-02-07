#include <iostream>
#include <vector>

using namespace std;

// Solution Code
class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {}
};
// ----

int main() {
  Solution s;

  // Example Input
  vector<int> nums = {2, 7, 11, 15};
  int target = 9;

  vector<int> result = s.twoSum(nums, target);

  // Example Output
  cout << "[" << result[0] << "," << result[1] << "\n";
  return 0;
}