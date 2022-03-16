#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

// 0-1 Knapsack Problem

typedef struct Item {
  int weight;
  int value;
} item;

int main() {
  int N, K;
  int w, v;
  std::cin >> N >> K;

  std::vector<item> items({{.weight = 0, .value = 0}});
  for (int n = 1; n <= N; n++) {
    std::cin >> w >> v;
    items.push_back({.weight = w, .value = v});
  }

  std::vector<std::vector<int>> maxValue;
  maxValue.assign(N + 1, std::vector<int>(K + 1, 0));

  for (int n = 1; n <= N; ++n) {
    for (int k = 1; k <= K; ++k) {
      auto item = items.at(n);
      if (item.weight > k) {
        maxValue[n][k] = maxValue[n - 1][k];
      } else {
        maxValue[n][k] = std::max(maxValue[n - 1][k - item.weight] + item.value,
                                  maxValue[n - 1][k]);
      }
    }
  }

  std::cout << maxValue[N][K] << std::endl;
  return 0;
}