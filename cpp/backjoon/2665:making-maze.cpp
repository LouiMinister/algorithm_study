#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>

using namespace std;

int N;
int area[51][51];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};
int res[51][51];

void dijkstra(int x, int y) {
  res[y][x] = 0;
  priority_queue<pair<int, pair<int, int>>> pq; // {cost, {x,y}}
  pq.push({0, {x, y}});

  while (!pq.empty()) {
    int nowX = pq.top().second.first;
    int nowY = pq.top().second.second;
    int nowCost = -pq.top().first;
    pq.pop();
    if (res[nowY][nowX] < nowCost)
      continue;
    for (int i = 0; i < 4; i++) {
      int nextX = nowX + dx[i];
      int nextY = nowY + dy[i];
      if (nextX <= 0 || nextY <= 0 || nextX > N || nextY > N)
        continue;
      int nextCost = nowCost + (1 - area[nextY][nextX]);
      if (res[nextY][nextX] > nextCost) {
        res[nextY][nextX] = nextCost;
        pq.push({-nextCost, {nextX, nextY}});
      }
    }
  }
}

int main() {
  fill_n(&res[0][0], 51 * 51, INT_MAX);
  cin >> N;
  string s;
  for (int i = 1; i <= N; i++) {
    cin >> s;
    for (int j = 1; j <= N; j++) {
      area[i][j] = s[j - 1] - '0';
    }
  }
  dijkstra(1, 1);

  // for (int i = 1; i <= N; i++) {
  //   for (int j = 1; j <= N; j++) {
  //     cout << res[i][j] << ' ';
  //   }
  //   cout << endl;
  // }

  cout << res[N][N];
}
