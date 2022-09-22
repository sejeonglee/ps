#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class State {
 public:
  int x;
  int y;
  int remained_move;
  int camp_number;
};

int solution(vector<string> grid, int k) {
  int answer = -1;
  const int n = static_cast<int>(grid.size());
  const int m = static_cast<int>(grid[0].size());

  vector<vector<int>> camp_visited(n, vector<int>());
  for (int i = 0; i < n; i++) {
    camp_visited[i].assign(m, 0);
  }

  queue<State> camp_queue;

  camp_visited[0][0] = 1;
  camp_queue.push({0, 0, k, 0});
  while (!camp_queue.empty()) {
    auto [camp_x, camp_y, camp_remained_move, camp_number] = camp_queue.front();
    cout << camp_x << ' ' << camp_y << ' ' << camp_number << endl;
    camp_queue.pop();

    // 다음 야영지 push
    queue<State> move_queue;
    move_queue = queue<State>();

    vector<vector<bool>> move_visited(n, vector<bool>());
    for (int i = 0; i < n; i++) {
      move_visited[i].assign(m, false);
    }

    move_visited[camp_x][camp_y] = true;
    move_queue.push({camp_x, camp_y, k, camp_number});

    while (!move_queue.empty()) {
      auto [x, y, remained_move, move_camp_number] = move_queue.front();
      move_queue.pop();
      if (x == n - 1 && y == m - 1) {
        answer = camp_number;
        return camp_number;
      }
      if (grid[x][y] == '.') {
        // 현재 위치가 평지이면 야영을 해봄
        if (!camp_visited[x][y]) {
          camp_visited[x][y] = 1;
          camp_queue.push({x, y, k, camp_number + 1});
        }
      }

      if (x - 1 >= 0 && grid[x - 1][y] != '#' && remained_move - 1 >= 0 &&
          !move_visited[x - 1][y]) {
        move_visited[x - 1][y] = true;
        move_queue.push({x - 1, y, remained_move - 1, move_camp_number});
      }
      if (x + 1 < n && grid[x + 1][y] != '#' && remained_move - 1 >= 0 &&
          !move_visited[x + 1][y]) {
        move_visited[x + 1][y] = true;
        move_queue.push({x + 1, y, remained_move - 1, move_camp_number});
      }
      if (y - 1 >= 0 && grid[x][y - 1] != '#' && remained_move - 1 >= 0 &&
          !move_visited[x][y - 1]) {
        move_visited[x][y - 1] = true;
        move_queue.push({x, y - 1, remained_move - 1, move_camp_number});
      }
      if (y + 1 < m && grid[x][y + 1] != '#' && remained_move - 1 >= 0 &&
          !move_visited[x][y + 1]) {
        move_visited[x][y + 1] = true;
        move_queue.push({x, y + 1, remained_move - 1, move_camp_number});
      }
    }
  }

  return answer;
}

int main() {
  vector<string> v = {"..FF", "###F", "###."};
  cout << solution(v, 4);
  return 0;
}