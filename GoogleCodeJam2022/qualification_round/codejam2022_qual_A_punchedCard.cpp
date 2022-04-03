#include <iostream>

using namespace std;

void printChar(int x, int y) {
  if (x <= 1 && y <= 1) {
    cout << ".";
    return;
  }
  bool rowIsOdd = x % 2;
  bool colIsOdd = y % 2;

  if (!rowIsOdd && !colIsOdd) {
    cout << "+";
  } else if (!rowIsOdd && colIsOdd) {
    cout << "-";
  } else if (rowIsOdd && !colIsOdd) {
    cout << "|";
  } else if (rowIsOdd && colIsOdd) {
    cout << ".";
  }
  return;
}

void process() {
  int R, C;
  cin >> R >> C;
  for (int x = 0; x <= 2 * R; x++) {
    for (int y = 0; y <= 2 * C; y++) {
      printChar(x, y);
    }
    cout << endl;
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    cout << "Case #" << i + 1 << ":";
    process();
  }

  return 0;
}