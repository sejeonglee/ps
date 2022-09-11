// https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b
#include <iostream>
#include <numeric>
#include <vector>

#define PRINT_REQUIRED 1000000

using namespace std;

void process() {
  // C, M, Y, K
  vector<int> min_ink;

  min_ink.assign(4, INT32_MAX);

  for (int i = 0; i < 3; i++) {
    int ink[4] = {0};
    cin >> ink[0] >> ink[1] >> ink[2] >> ink[3];

    for (int j = 0; j < 4; j++) {
      if (min_ink[j] > ink[j]) {
        min_ink[j] = ink[j];
      }
    }
  }

  vector<int> answer(min_ink);
  for (int i = 0; i < 4; i++) {
    int sum_ink = accumulate(answer.begin(), answer.end(), 0);
    if (sum_ink < PRINT_REQUIRED) {
      answer.clear();
      break;
    } else {
      answer[i] = max(0, answer[i] - (sum_ink - PRINT_REQUIRED));
    }
  }

  if (answer.empty()) {
    cout << "IMPOSSIBLE";
  } else {
    for (auto&& ink : answer) {
      cout << ink << " ";
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    cout << "Case #" << i + 1 << ": ";
    process();
    cout << endl;
  }

  return 0;
}