#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <utility>
#include <vector>

using namespace std;
int N, V, D, S;                      // 노드, 간선, 거리, 시작노드
vector<pair<int, int>> adj[1123456]; // {노드 , cost}

vector<int> dijkstra(int src) {
  vector<int> dist(N + 1, INT_MAX);
  dist[src] = 0;
  priority_queue<pair<int, int>> pq; // {cost, node}
  pq.push({0, src});
  while (!pq.empty()) {
    int nowCost = -pq.top().first;
    int nowNode = pq.top().second;
    pq.pop();
    if (dist[nowNode] < nowCost)
      continue;
    for (int i = 0; i < adj[nowNode].size(); i++) {
      int nextNode = adj[nowNode][i].first;
      int costSum = nowCost + adj[nowNode][i].second;
      if (dist[nextNode] > costSum) {
        dist[nextNode] = costSum;
        pq.push({-costSum, nextNode});
      }
    }
  }
  return dist;
}

int main() {
  cin >> N >> V >> D >> S;

  int in1, in2;
  for (int i = 0; i < V; i++) {
    cin >> in1 >> in2;
    adj[in1].push_back({in2, 1});
  }
  vector<int> res = dijkstra(S);
  bool ansFlag = false;
  for (int i = 1; i <= N; i++) {
    if (res[i] == D) {
      cout << i << '\n';
      ansFlag = true;
    }
  }
  if (!ansFlag) {
    cout << -1;
  }
}
