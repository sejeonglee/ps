// https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471
#include <algorithm>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <utility>
#include <vector>

using namespace std;
typedef pair<int, int> pii;

void process() {
  int N;
  cin >> N;

  vector<int> vec;

  vec.push_back(0);
  for (int i = 1; i <= N; ++i) {
    int side_numbers;
    cin >> side_numbers;
    vec.push_back(side_numbers);
  }

  sort(vec.begin(), vec.end());

  int max_deviation = 0;
  for (int i = 1; i <= N; i++) {  // n

    if ((i - vec[i]) > max_deviation) {
      max_deviation = i - vec[i];
    }
  }

  int answer = N - max_deviation;
  cout << answer;
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