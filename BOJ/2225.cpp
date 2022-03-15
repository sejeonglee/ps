#include <iostream>
#include <numeric>
#include <vector>

typedef std::vector<int>::iterator vit;
int vector_sum(vit begin, vit end) {
  int sum = 0;
  while (begin != end) {
    sum = (sum + (*begin) % 1000000000) % 1000000000;
    begin++;
  }
  return sum;
}

int main() {
  int N, K;
  std::cin >> N >> K;

  std::vector<std::vector<int>> v;

  v.assign(K + 1, std::vector<int>(N + 1, 1));

  for (int k = 2; k <= K; ++k) {
    for (int n = 1; n <= N; ++n) {
      v[k][n] = vector_sum(v[k - 1].begin(), v[k - 1].begin() + (n + 1));
    }
  }

  std::cout << v[K][N] % 1000000000 << std::endl;
  return 0;
}