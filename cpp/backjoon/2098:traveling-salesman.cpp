#include <cstring>
#include <iostream>
#define INF 999999999
#define MAX 16
#define UNVISITED -1
using namespace std;

int N;
int w[MAX][MAX];
int dp[MAX][1 << MAX];

void input() {
  cin >> N;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      cin >> w[i][j];
  memset(dp, UNVISITED, sizeof(dp));
}

int dfs(int start, int end) {
  if (dp[start][end] != UNVISITED)
    return dp[start][end];

  if (end == (1 << N) - 1) {
    if (w[start][0] != 0)
      return w[start][0];
    return INF;
  }
  dp[start][end] = INF;
  for (int i = 0; i < N; ++i) {
    if (end & (1 << i) || w[start][i] == 0)
      continue;
    dp[start][end] = min(dp[start][end], dfs(i, end | (1 << i)) + w[start][i]);
  }
  return dp[start][end];
}
int main() {
  input();
  cout << dfs(0, 1) << endl;
  return 0;
}
