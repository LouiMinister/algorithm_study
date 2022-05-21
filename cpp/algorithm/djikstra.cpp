#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <utility>
#include <vector>

// 18352번 문제

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
