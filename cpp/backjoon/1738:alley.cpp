#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <utility>
#include <vector>

using namespace std;
const long long MININF = LLONG_MIN / 10;
const long long MAXINF = LLONG_MAX / 10;

int N, E;                        // node, edge
vector<pair<int, int>> adj[101]; // {node ,cost}

vector<pair<long long, vector<int>>> bellmanFord(int src) {
  vector<pair<long long, vector<int>>> res(N + 1,
                                           make_pair(MININF, vector<int>()));
  res[src] = {0, {1}};
  bool updated;
  for (int i = 1; i <= N; i++) {
    updated = false;
    for (int nowNode = 1; nowNode <= N; nowNode++) {
      if (res[nowNode].first == MININF) // 처음 시작 노드와 연결이 안됐을 경우
        continue;
      for (int j = 0; j < adj[nowNode].size(); j++) {
        int toNode = adj[nowNode][j].first;
        int edgeCost = adj[nowNode][j].second;
        if (res[toNode].first < res[nowNode].first + edgeCost) {
          res[toNode].first = res[nowNode].first + edgeCost;
          res[toNode].second = vector<int>(res[nowNode].second);
          res[toNode].second.push_back(toNode);
          if (i == N) {
            res[toNode].first = MAXINF;
            res[toNode].second.clear();
          }
          updated = true;
        }
      }
    }
    if (!updated) // relax가 한번도 되지 않았을 경우 종료
      break;
  }
  // if (updated) // N번 돌 때 relax가 된 경우 음의 루프
  // res.clear();
  return res;
}

int main() {
  cin >> N >> E;
  int in1, in2, in3;
  for (int i = 1; i <= E; i++) {
    cin >> in1 >> in2 >> in3;
    adj[in1].push_back({in2, in3});
  }
  vector<pair<long long, vector<int>>> res = bellmanFord(1);
  if (res[N].first == MAXINF) {
    cout << -1;
  } else {
    for (int v : res[N].second) {
      cout << v << ' ';
    }
  }
}
