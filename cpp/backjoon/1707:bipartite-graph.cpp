#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <stack>
#include <vector>
using namespace std;

int TC;
int V, E;
vector<int> adj[21234];
int visited[21234];
vector<string> out;

bool dfs(int src) { // true - 이분인 경우, false - 이분이 아닌 경우
  stack<int> st;    // node
  st.push(src);
  visited[src] = 1;
  while (!st.empty()) {
    int curNode = st.top();
    st.pop();

    for (int i = 0; i < adj[curNode].size(); i++) {
      int toNode = adj[curNode][i];
      if (visited[toNode] == 0) { // 방문 안한경우
        visited[toNode] = -visited[curNode];
        st.push(toNode);
      } else {                                     // 이미 방문 한 경우
        if (visited[toNode] == visited[curNode]) { // 접하는 경우
          return false;
        }
      }
    }
  }
  return true;
}

int main() {
  cin >> TC;
  for (int t = 1; t <= TC; t++) {
    cin >> V >> E;
    int in1, in2;
    for (int i = 1; i <= E; i++) {
      cin >> in1 >> in2;
      adj[in1].push_back(in2);
      adj[in2].push_back(in1);
    }

    for (int i = 1; i <= V; i++) {
      if (visited[i] == 0) {
        bool res = dfs(i);
        if (res == false) {
          out.push_back("NO");
          break;
        }
      }
      if (i == V) {
        out.push_back("YES");
      }
    }

    for (int i = 1; i <= V; i++) { // init
      adj[i].clear();
      visited[i] = 0;
    }
  }

  for (string s : out) {
    cout << s << '\n';
  }
}
