#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

// Solution Code
class Solution {
 public:
  int findMaxK(vector<int>& nums) {
    int max_k = -1;
    unordered_set<int> waiting_set;
    for (auto num : nums) {
      if (waiting_set.find(num) != waiting_set.end()) {
        max_k = max(max_k, abs(num));
      } else {
        waiting_set.insert(-num);
      }
    }

    return max_k;
  }
};
// ----

int main() {
  Solution sol;

  // Example Input
  vector<int> nums = {3, 2, 4};

  int result = sol.findMaxK(nums);

  cout << result << "\n";
  return 0;
}