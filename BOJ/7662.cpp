#include <iostream>
#include <set>

// Multiset 사용하는 걸 깜빡했다. 문제 조건에 중복된 값이 있을 수 있다는 것을
// 확인

void process() {
  int K;
  char type;
  int value;
  std::multiset<int> dualPQ;
  std::cin >> K;
  for (int i = 0; i < K; i++) {
    std::cin >> type >> value;

    if (type == 'I') {
      dualPQ.insert(value);
    } else if (type == 'D' && !dualPQ.empty()) {
      if (value == 1) {
        std::multiset<int>::iterator endIt(--dualPQ.rbegin().base());
        dualPQ.erase(endIt);
      } else if (value == -1) {
        dualPQ.erase(dualPQ.begin());
      }
    }
  }
  if (dualPQ.empty()) {
    std::cout << "EMPTY" << std::endl;
  } else {
    std::cout << *dualPQ.rbegin() << " " << *dualPQ.begin() << std::endl;
  }
}

int main() {
  int T;
  std::cin >> T;

  for (int i = 0; i < T; i++) {
    process();
  }

  return 0;
}