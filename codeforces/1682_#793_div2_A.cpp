// https://codeforces.com/contest/1682/problem/A
#include <bits/stdc++.h>

using namespace std;

void solve() {
  int n;
  string s;
  cin >> n;
  cin >> s;

  int answer = 0;
  char pivot = s[n / 2];
  for (int j = n / 2 - 1; j >= 0; j--) {
    if (s[j] == pivot) {
      answer += 2;
    } else {
      break;
    }
  }
  if (n % 2 == 1) {
    answer++;
  }
  cout << answer << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  // Test Cases T
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    solve();
  }

  return 0;
}
