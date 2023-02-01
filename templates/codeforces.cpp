#include <iostream>

using namespace std;

void process() {
  int answer = 10;

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