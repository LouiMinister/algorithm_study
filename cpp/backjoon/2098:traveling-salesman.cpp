#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

int path[16][16]; // distance i -> j
int minDistance[(1 << 16)][16];
int N;
int maxV = 10000;
int allVisited;

int dfs(int visited, int cur) {
  if (visited == allVisited) { // 전부 방문했을 경우
    if (path[cur][0] != 0) {
      return path[cur][0];
    } else {
      return maxV;
    }
  }

  int cost = minDistance[visited][cur];
  if (cost != -1) {
    return cost;
  } else {
    minDistance[visited][cur] = maxV;
  }

  for (int i = 0; i < N; i++) {
    int z = ~visited;
    int a = ~visited & (1 << i);
    if ((~visited & (1 << i)) && (path[cur][i] != 0)) {
      int nextVisited = visited | (1 << i);
      minDistance[visited][cur] =
          min(minDistance[visited][cur], dfs(nextVisited, cur) + path[cur][i]);
    }
  }
  return minDistance[visited][cur];
}

int main() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> path[i][j];
    }
  }
  memset(minDistance, -1, sizeof(minDistance));
  allVisited = (1 << N) - 1;

  cout << dfs(1, 0) << endl;
}
