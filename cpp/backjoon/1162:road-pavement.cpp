#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

int N, V, K;
vector<pair<int, int>> adj[11234];

vector<vector<long long>> dijkstra(int src) {
  vector<vector<long long>> res(
      K + 1, vector<long long>(N + 1, LLONG_MAX)); // [포장도로수][노드]
  res[0][src] = 0;
  priority_queue<vector<long long>> pq; // cost, node, 포장도로수
  pq.push({-0, src, 0});

  while (!pq.empty()) {
    long long nowCost = -pq.top()[0];
    long long nowNode = pq.top()[1];
    long long nowPaveCnt = pq.top()[2];
    pq.pop();
    if (nowCost > res[nowPaveCnt][nowNode])
      continue;

    for (int i = 0; i < adj[nowNode].size(); i++) {
      long long nextNode = adj[nowNode][i].first;
      long long costSum = nowCost + adj[nowNode][i].second;
      if (res[nowPaveCnt][nextNode] > costSum) {
        res[nowPaveCnt][nextNode] = costSum;
        pq.push({-costSum, nextNode, nowPaveCnt});
      }
      if (nowPaveCnt < K) { // 포장할 수 있는 기회가 남은 경우
        if (res[nowPaveCnt + 1][nextNode] > nowCost) {
          res[nowPaveCnt + 1][nextNode] = nowCost;
          pq.push({-nowCost, nextNode, nowPaveCnt + 1});
        }
      }
    }
  }
  return res;
}

int main() {
  cin >> N >> V >> K;
  int e1, e2, c;
  for (int i = 0; i < V; i++) {
    cin >> e1 >> e2 >> c;
    adj[e1].push_back({e2, c});
    adj[e2].push_back({e1, c});
  }

  vector<vector<long long>> res = dijkstra(1);
  long long ans = LLONG_MAX;
  for (int i = 1; i <= K; i++) {
    ans = min(ans, res[i][N]);
  }
  cout << ans << endl;
}
