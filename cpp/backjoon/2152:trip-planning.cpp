#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <vector>

using namespace std;

int V, E, S, T;
vector<int> v[11234];
vector<int> rv[11234];
vector<int> scc[11234];
pair<int, set<int>> sccNode[11234];
int belongIn[11234];
int visited[11234];
stack<int> st;
int res = 0;

int sccCnt = 0;

void dfs(int n) {
  visited[n] = true;
  for (auto nn : v[n]) {
    if (visited[nn])
      continue;
    dfs(nn);
  }
  st.push(n);
}

void rdfs(int n) {
  visited[n] = true;
  scc[sccCnt].push_back(n);
  belongIn[n] = sccCnt;
  for (auto nn : rv[n]) {
    if (visited[nn])
      continue;
    rdfs(nn);
  }
}

void bfs(int node) {
  pair<int, set<int>> sNode = sccNode[node];
  int sSum = sNode.first;
  queue<pair<int, int>> qu;
  qu.push({node, sSum}); // 노드, 합
  visited[node] = sSum;

  while (!qu.empty()) {
    pair<int, int> front = qu.front();
    int frontSccNode = front.first;
    int frontSum = front.second;
    qu.pop();

    if (frontSccNode == belongIn[T]) {
      res = max(res, frontSum);
      continue;
    }
    set<int> nextSccNodes = sccNode[frontSccNode].second;
    for (int nextSccNode : nextSccNodes) {
      pair<int, int> newPair;
      newPair.first = nextSccNode;
      newPair.second = frontSum + sccNode[nextSccNode].first;
      if (visited[nextSccNode] < newPair.second) {
        visited[nextSccNode] = newPair.second;
        qu.push(newPair);
      }
    }
  }
}

int main() {
  cin >> V >> E >> S >> T;

  int input1, input2;
  for (int i = 1; i <= E; i++) {
    cin >> input1 >> input2;
    v[input1].push_back(input2);
    rv[input2].push_back(input1);
  }

  for (int i = 1; i <= V; i++) {
    if (!visited[i]) {
      dfs(i);
    }
  }
  fill_n(visited, 11234, false);
  while (!st.empty()) {
    int top = st.top();
    st.pop();
    if (!visited[top]) {
      sccCnt++;
      rdfs(top);
    }
  }

  for (int i = 1; i <= sccCnt; i++) {
    sccNode[i].first = 0;
    for (auto node : scc[i]) {
      vector<int> nodeArrows = v[node];
      for (auto nodeTo : nodeArrows) {
        int sccNodeTo = belongIn[nodeTo];
        if (sccNodeTo != i)
          sccNode[i].second.insert(sccNodeTo);
      }
      sccNode[i].first++;
    }
  }
  fill_n(visited, 11234, false);
  bfs(belongIn[S]);
  cout << res << endl;
}
