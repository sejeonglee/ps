#include <iostream>
#include <stack>
#include <utility>

int searchTower(std::stack<std::pair<int, int>>& stk, int height) {
  while (!stk.empty()) {
    if (stk.top().first >= height) {
      return stk.top().second;
    }
    stk.pop();
  }
  return 0;
}

int main() {
  std::ios::sync_with_stdio(0);
  std::cin.tie(0);
  int N;
  std::cin >> N;

  // Pair first -> height, second = index
  std::stack<std::pair<int, int>> towers;
  int height;
  for (int i = 1; i <= N; i++) {
    std::cin >> height;
    std::cout << searchTower(towers, height) << " ";
    towers.push({height, i});
  }

  return 0;
}