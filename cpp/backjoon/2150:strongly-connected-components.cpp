#include <algorithm>
#include <cmath>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int V, E;
vector<int> v[11234];
vector<int> rv[11234];
vector<int> scc[11234];
bool visited[11234];
stack<int> st;

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
  for (auto nn : rv[n]) {
    if (visited[nn])
      continue;
    rdfs(nn);
  }
}

bool cmp(vector<int> a, vector<int> b) { return a[0] < b[0]; }

int main() {
  cin >> V >> E;

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
      sort(scc[sccCnt].begin(), scc[sccCnt].end());
    }
  }
  cout << sccCnt << '\n';

  sort(scc + 1, scc + 1 + sccCnt, cmp);
  int i = 1;
  while (true) {
    if (scc[i].empty())
      break;
    for (auto v : scc[i]) {
      cout << v << ' ';
    }
    cout << -1 << '\n';
    i++;
  }
}
