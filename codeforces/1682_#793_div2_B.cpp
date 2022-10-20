// https://codeforces.com/contest/1682/problem/B
#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;

void process() {
  int answer;

  int n;  // length of purmutation
  cin >> n;

  vector<pii> input_permutation;
  for (int i = 0; i < n; i++) {
    int p_i;
    cin >> p_i;
    input_permutation.push_back({p_i, i});
  }
  sort(input_permutation.begin(), input_permutation.end());

  vector<int> need_to_swap_indices;
  for (int i = 0; i < input_permutation.size(); i++) {
    if (input_permutation[i].second != i)
      need_to_swap_indices.push_back(input_permutation[i].second);
  }

  answer = need_to_swap_indices[0];
  for (auto &&index : need_to_swap_indices) {
    answer = answer & index;
  }

  cout << answer << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);

  int T;
  cin >> T;

  for (int i = 1; i <= T; i++) {
    process();
  }

  return 0;
}