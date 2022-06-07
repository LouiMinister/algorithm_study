#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <stack>
#include <vector>

using namespace std;

const int MV = 5050;

int V, E;
int in1, in2;
vector<int> adj[MV];
vector<int> radj[MV];
bool vis[MV];
stack<int> st;
int groupCnt = 0;
int belongIn[MV];
vector<int> group[MV];

void dfs(int src) {
  vis[src] = true;
  for (int i = 0; i < adj[src].size(); i++) {
    int next = adj[src][i];
    if (!vis[next]) {
      dfs(next);
    }
  }
  st.push(src);
}

void rdfs(int src) {
  vis[src] = true;
  group[groupCnt].push_back(src);
  belongIn[src] = groupCnt;
  for (int i = 0; i < radj[src].size(); i++) {
    int next = radj[src][i];
    if (!vis[next]) {
      rdfs(next);
    }
  }
}

void clear() {
  for (int i = 1; i <= V; i++) {
    vis[i] = false;
    belongIn[i] = 0;
    adj[i].clear();
    radj[i].clear();
  }
  for (int i = 1; i <= groupCnt; i++) {
    group[i].clear();
  }
  groupCnt = 0;
}

int main() {
  while (true) {
    cin >> V;
    if (V == 0)
      break;
    cin >> E;
    for (int i = 1; i <= E; i++) {
      cin >> in1 >> in2;
      adj[in1].push_back(in2);
      radj[in2].push_back(in1);
    }

    for (int i = 1; i <= V; i++) {
      if (!vis[i])
        dfs(i);
    }
    fill_n(vis, V + 1, false);

    while (!st.empty()) {
      int n = st.top();
      st.pop();
      if (!vis[n]) {
        groupCnt++;
        rdfs(n);
      }
    }

    vector<int> ans;
    bool opp;
    for (int g = 1; g <= groupCnt; g++) {
      opp = true;
      for (int v : group[g]) { // 그룹에 속해있는 정점
        if (opp == false)
          break;
        for (int i = 0; i < adj[v].size(); i++) { // 정점의 인접 순회
          int next = adj[v][i];
          if (belongIn[next] != g) { // 다른 그룹으로 향하는 간선이 있는 경우
            opp = false; // 그룹은 가망이 없다
            break;
          }
        }
      }
      if (opp == true) {
        for (int v : group[g]) {
          ans.push_back(v);
        }
      }
    }
    sort(ans.begin(), ans.end());
    for (int i : ans)
      cout << i << ' ';
    cout << endl;
    clear();
  }
}
