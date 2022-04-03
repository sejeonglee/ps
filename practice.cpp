#include <iostream>
#include <queue>
#include <tuple>
#include <utility>
#include <vector>

#define INF 1000000000

using namespace std;

typedef pair<int, int> pii;

vector<vector<pii>> edges;
vector<int> dist;
vector<bool> visited;

priority_queue<pii, vector<pii>, greater<pii>> priorityQueue;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int V, E;
  int K;
  int u, v, w;

  cin >> V >> E;
  cin >> K;

  edges.assign(V + 1, vector<pii>(0));
  visited.assign(V + 1, false);
  dist.assign(V + 1, INF);

  for (int i = 0; i < E; i++) {
    cin >> u >> v >> w;
    edges[u].push_back({v, w});
  }

  dist[K] = 0;
  priorityQueue.push({0, K});
  while (!priorityQueue.empty()) {
    int currentDist, searchNode;
    tie(currentDist, searchNode) = priorityQueue.top();
    priorityQueue.pop();

    if (visited[searchNode]) {
      continue;
    }
    visited[searchNode] = true;

    for (auto &&pair : edges[searchNode]) {
      int to, weight;
      tie(to, weight) = pair;

      if (dist[to] > dist[searchNode] + weight) {
        dist[to] = dist[searchNode] + weight;
        priorityQueue.push({to, dist[to]});
      }
    }
  }

  for (int i = 1; i <= V; i++) {
    if (dist[i] == INF) {
      cout << "INF" << endl;
    } else {
      cout << dist[i] << endl;
    }
  }

  return 0;
}