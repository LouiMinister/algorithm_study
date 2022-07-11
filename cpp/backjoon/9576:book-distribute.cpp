#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>

using namespace std;

int TC;
int B, S;
pair<int, int> SV[1234];
bool vis[1234];
int occBy[1234];

bool dfs(int fromNode) {
  for (int i = SV[fromNode].first; i <= SV[fromNode].second; i++) { // toNode
    if (vis[i])
      continue;
    vis[i] = true;
    if (occBy[i] == 0 || dfs(occBy[i])) {
      occBy[i] = fromNode;
      return true;
    }
  }
  return false;
}

int main() {
  cin >> TC;
  int in1, in2;
  for (int T = 1; T <= TC; T++) {
    cin >> B >> S;
    for (int i = 1; i <= S; i++) {
      cin >> in1 >> in2;
      SV[i] = {in1, in2};
    }
    int cnt = 0;
    fill_n(occBy, 1234, 0);
    for (int i = 1; i <= S; i++) {
      fill_n(vis, 1234, false);
      if (dfs(i))
        cnt++;
    }
    cout << cnt << '\n';
  }
}
