#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <string>

using namespace std;
int H, W;
int maze[101][101];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int bfs() {
  int dist[101][101];
  fill_n(&dist[0][0], 101 * 101, 0);
  queue<pair<int, int>> q;
  dist[1][1] = 1;
  q.push({1, 1});
  while (!q.empty()) {
    pair<int, int> cur = q.front(); // x y
    q.pop();
    for (int i = 0; i < 4; i++) {
      int x = cur.first + dx[i];
      int y = cur.second + dy[i];
      if (x >= 1 && x <= W && y >= 1 && y <= H && maze[y][x] == 1 &&
          dist[y][x] == 0) {
        pair<int, int> nxt = {x, y};
        q.push(nxt);
        dist[y][x] = dist[cur.second][cur.first] + 1;
        if (x == W && y == H) {
          return dist[H][W];
        }
      }
    }
  }
  return 0;
}

int main() {
  cin >> H >> W;
  cin.ignore();
  for (int i = 1; i <= H; i++) {
    string in;
    getline(cin, in);
    for (int j = 1; j <= W; j++) {
      maze[i][j] = in[j - 1] - '0';
    }
  }
  cout << bfs() << endl;
  // cout << endl;
  // for (int i = 1; i <= H; i++) {
  //   for (int j = 1; j <= W; j++) {
  //     cout << maze[i][j] << ' ';
  //   }
  //   cout << endl;
  // }
}
