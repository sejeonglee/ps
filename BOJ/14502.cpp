#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

int n, m;

vector<pii> virus;
vector<pii> wall_cand;
int test_with_three_walls(vector<pii> walls, vector<vector<int>> arr) {
  vector<vector<int>> test_arr(arr);

  for (auto wall : walls) {
    test_arr[wall.first][wall.second] = 1;
  }

  // initial Queue
  queue<pii> q;
  for (auto virus : virus) {
    q.push(virus);
  }

  vector<pii> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  vector<vector<bool>> visited(n, vector<bool>(m, false));

  while (!q.empty()) {
    pii cur = q.front();
    q.pop();

    test_arr[cur.first][cur.second] = 2;
    visited[cur.first][cur.second] = true;

    for (auto dir : directions) {
      int nx = cur.first + dir.first;
      int ny = cur.second + dir.second;

      if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
        continue;
      }

      if (test_arr[nx][ny] == 0 && !visited[nx][ny]) {
        visited[nx][ny] = true;
        q.push({nx, ny});
      }
    }
  }

  int count = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (test_arr[i][j] == 0) {
        count++;
      }
    }
  }
  return count;
}

int main() {
  cin >> n >> m;

  vector<vector<int>> map(n, vector<int>(m, 0));

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cin >> map[i][j];
      if (map[i][j] == 0) {
        wall_cand.push_back({i, j});
      } else if (map[i][j] == 2) {
        virus.push_back({i, j});
      }
    }
  }
  int answer = 0;
  for (int i = 0; i < wall_cand.size(); i++) {
    for (int j = i + 1; j < wall_cand.size(); j++) {
      for (int k = j + 1; k < wall_cand.size(); k++) {
        vector<pii> walls = {wall_cand[i], wall_cand[j], wall_cand[k]};
        answer = max(answer, test_with_three_walls(walls, map));
      }
    }
  }

  cout << answer;

  return 0;
}