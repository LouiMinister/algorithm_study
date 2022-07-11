#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <vector>

using namespace std;

int V, E;
vector<vector<int>> adj;
int resDist;          // 제일 먼 노드까지의 길이
vector<int> resNodes; // 제일 먼 노드들의 목록

void bfs() {
  vector<bool> visited(V + 1);
  queue<pair<int, int>> q; // node, dist
  visited[1] = true;
  q.push({1, 0});
  while (!q.empty()) {
    int curNode = q.front().first;
    int curDist = q.front().second;
    q.pop();
    if (resDist < curDist) {
      resDist = curDist;
      resNodes.clear();
    }
    resNodes.push_back(curNode);
    for (int nxt : adj[curNode]) {
      if (visited[nxt])
        continue;
      q.push({nxt, curDist + 1});
      visited[nxt] = true;
    }
  }
}

int main() {
  cin >> V >> E;
  adj.resize(V + 1, vector<int>(0));
  int in1, in2;
  for (int i = 1; i <= E; i++) {
    cin >> in1 >> in2;
    adj[in1].push_back(in2);
    adj[in2].push_back(in1);
  }
  bfs();
  cout << *min_element(resNodes.begin(), resNodes.end()) << ' ' << resDist
       << ' ' << resNodes.size();
}
