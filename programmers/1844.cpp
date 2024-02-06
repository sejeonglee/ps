#include <algorithm>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int, pair<int, int>> point;

int solution(vector<vector<int>> maps) {
  int N = maps.size();
  int M = maps[0].size();
  int answer = 0;

  queue<point> q;
  q.push({1, {0, 0}});

  vector<vector<bool>> visited(maps.size(),
                               vector<bool>(maps[0].size(), false));
  visited[0][0] = true;
  pair<int, int> directions[] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

  while (!q.empty()) {
    auto cur = q.front();
    int cur_step = cur.first;
    auto cursor = cur.second;
    q.pop();

    for (auto dir : directions) {
      int nx = cursor.first + dir.first;
      int ny = cursor.second + dir.second;

      if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny]) {
        continue;
      } else if (nx == N - 1 && ny == M - 1) {
        return cur_step + 1;
      } else if (maps[nx][ny] == 1) {
        visited[nx][ny] = true;
        q.push({cur_step + 1, {nx, ny}});
      }
    }
  }
  return -1;
}