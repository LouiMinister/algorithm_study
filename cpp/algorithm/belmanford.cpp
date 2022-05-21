#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <utility>
#include <vector>

using namespace std;

vector<pair<int, int>> adj[501]; // {node ,cost}
int N, E;

vector<long long> bellmanFord(int src) {
  vector<long long> res(N + 1, LLONG_MAX);
  res[src] = 0;

  bool updated;
  for (int i = 1; i <= N; i++) { // N번 순회
    updated = false;
    for (int nowNode = 1; nowNode <= N; nowNode++) {
      for (int j = 0; j < adj[nowNode].size(); j++) {
        int toNode = adj[nowNode][j].first;
        int edgeCost = adj[nowNode][j].second;
        if (res[nowNode] ==
            LLONG_MAX) // 기존 노드가 시작점과 연결되지 않는 경우
          continue;
        if (res[toNode] > res[nowNode] + edgeCost) {
          res[toNode] = res[nowNode] + edgeCost;
          // if (i == N) {
          //   res[toNode] = INT_MIN;
          // }
          updated = true;
        }
      }
    }
    if (!updated) // relax가 하나라도 없을 경우 경우 종료
      break;
  }
  if (updated) // N-1만큼  돌고 나서도 완화가 이루어 졌을 경우 -> 음의 순환 존재
    res.clear();

  return res;
}
