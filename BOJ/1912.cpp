#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> v;
  v.assign(n, 0);

  vector<int> dp;
  dp.assign(n, 0);

  for (int i = 0; i < n; ++i) {
    cin >> v[i];
  }

  dp[0] = v[0];

  for (int i = 1; i < n; ++i) {
    dp[i] = max(dp[i - 1] + v[i], v[i]);
  }

  cout << *max_element(dp.begin(), dp.end()) << endl;
  return 0;
}