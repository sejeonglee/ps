#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

// Solution Code
class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> result;
    unordered_map<int, int> complement_index;
    for (size_t i = 0; i < nums.size(); i++) {
      if (complement_index.find(nums[i]) != complement_index.end()) {
        result.push_back(complement_index[nums[i]]);
        result.push_back(i);
        return result;
      }
      int complement = target - nums[i];
      complement_index[complement] = i;
    }

    return result;
  }
};
// ----

int main() {
  Solution s;

  // Example Input
  vector<int> nums = {3,2,4};
  int target = 6;

  vector<int> result = s.twoSum(nums, target);

  cout << "[" << result[0] << "," << result[1] << "]\n";
  return 0;
}