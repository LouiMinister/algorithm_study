#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <vector>
using namespace std;

int N, M;
int S, E;
vector<pair<int, int>> adj[1234]; // vertex, cost

vector<int> dijkstra(int src) {
  vector<int> dist(N + 1, INT_MAX);
  priority_queue<pair<int, int>> q; // dist, node
  q.push({0, src});
  dist[src] = 0;
  while (!q.empty()) {
    int curDist = -q.top().first;
    int curNode = q.top().second;
    q.pop();
    if (dist[curNode] < curDist)
      continue;
    for (int i = 0; i < adj[curNode].size(); i++) {
      int toNode = adj[curNode][i].first;
      int toDist = curDist + adj[curNode][i].second;
      if (toDist < dist[toNode]) {
        dist[toNode] = toDist;
        q.push({-toDist, toNode});
      }
    }
  }
  return dist;
}

int main() {
  cin >> N >> M;
  int in1, in2, in3;
  for (int i = 0; i < M; i++) {
    cin >> in1 >> in2 >> in3;
    adj[in1].push_back({in2, in3});
  }
  cin >> S >> E;
  vector<int> dist = dijkstra(S);
  cout << dist[E];
}
