#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>

using namespace std;

int F, S, G, U, D;
bool vis[1123123];
queue<pair<int, int>> q; // 현재층, 버튼 누른 횟수

int bfs(int src) {
  q.push({src, 0});
  vis[src] = true;
  int cand[] = {U, -D};
  while (!q.empty()) {
    int now = q.front().first;
    int cnt = q.front().second;
    q.pop();
    for (int i = 0; i < 2; i++) {
      int next = now + cand[i];
      if (next < 1 || next > F)
        continue;
      if (vis[next])
        continue;

      if (next == G)
        return cnt + 1;
      vis[next] = true;
      q.push({next, cnt + 1});
    }
  }
  return -1;
}

int main() {
  cin >> F >> S >> G >> U >> D;
  if (S == G) {
    cout << 0;
    return 0;
  }
  int res = bfs(S);
  if (res == -1) {
    cout << "use the stairs";
  } else {
    cout << res;
  }
}
