#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <vector>

using namespace std;

int N, M, K; // 1<=N,M<+1000, 1<=K<=N
vector<int> adj[1010];
bool vis[1010];
int occBy[1010];

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
  for (int i = 1; i <= N; i++) {
    fill_n(vis, 1010, false);
    if (dfs(i))
      cnt++;
  }

  for (int i = 1; i <= N; i++) {
    fill_n(vis, 1010, false);
    if (dfs(i)) {
      cnt++;
      K--;
    }
    if (K == 0)
      break;
  }

  return cnt;
}

int main() {
  cin >> N >> M >> K;
  int in1, in2;
  for (int i = 1; i <= N; i++) {
    cin >> in1;
    for (int j = 1; j <= in1; j++) {
      cin >> in2;
      adj[i].push_back(in2);
    }
  }
  cout << bipartite();
}
