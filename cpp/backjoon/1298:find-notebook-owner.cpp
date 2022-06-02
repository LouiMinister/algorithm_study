#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <set>
#include <vector>

using namespace std;

int N, M; // 사람수 1 100, 노트북수 0 5000
vector<int> adj[123];
set<int> pAry;
bool vis[5050];
int occBy[5050];

bool dfs(int from) {
  for (int to : adj[from]) {
    if (vis[to])
      continue;
    vis[to] = true;
    if (occBy[to] == 0 || dfs(occBy[to])) {
      occBy[to] = from;
      return true;
    }
  }
  return false;
}

int bipartite() {
  int cnt = 0;
  for (int i : pAry) {
    fill_n(vis, 5050, false);
    if (dfs(i))
      cnt++;
  }
  return cnt;
}

int main() {
  cin >> N >> M;
  int in1, in2;
  for (int i = 1; i <= M; i++) {
    cin >> in1 >> in2;
    adj[in1].push_back(in2);
    pAry.insert(in1);
  }
  cout << bipartite();
}
