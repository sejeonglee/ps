#include <iostream>

using namespace std;

char determine(int n, int i, int j) {
  if (n == 3) {
    if (i == 2 && j == 2) {
      return ' ';
    } else {
      return '*';
    }
  } else if( ( n/3 < i && i <= (2 * n/3) )
            && ( n/3 < j && j <= (2 * n/3) )){
    return ' ';
  } else {
      return determine(n/3, i%(n/3), j%(n/3));
  }
}

int main() {
  int N;
  scanf("%d", &N);

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      printf("%c", determine(N, i, j));
    }
    printf("\n");
  }

  return 0;
}