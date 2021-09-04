// https://www.acmicpc.net/problem/2447

// 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할
// 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

// 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩
// 있는 패턴이다.

// ***
// * *
// ***

// N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3)
// 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은
// 예제 출력 1과 같다.

#include <iostream>

using namespace std;

char determine(int n, int i, int j) {
  if (n == 3) {
    if (i == 2 && j == 2) {
      return ' ';
    } else {
      return '*';
    }
  } else if ((n / 3 < i && i <= (2 * n / 3)) &&
             (n / 3 < j && j <= (2 * n / 3))) {
    return ' ';
  } else {
    return determine(n / 3, i % (n / 3), j % (n / 3));
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