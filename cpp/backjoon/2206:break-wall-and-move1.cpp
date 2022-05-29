#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>

using namespace std;

int H, W;
int area[1001][1001];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
bool visited[1001][1001][2]; // [y][x][부순횟수]

int bfs() {
  queue<pair<pair<int, int>, pair<int, int>>> q; // {{x,y}, {부순횟수, 거리}
  q.push({{1, 1}, {0, 1}});
  while (!q.empty()) {
    int x = q.front().first.first;
    int y = q.front().first.second;
    int bc = q.front().second.first;
    int dist = q.front().second.second;
    q.pop();
    if (x == W && y == H)
      return dist;
    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (nx >= 1 && ny >= 1 && nx <= W && ny <= H) {
        if (bc == 0 && area[ny][nx] == 1 &&
            !visited[ny][nx][1]) { // 부수는 경우
          q.push({{nx, ny}, {bc + 1, dist + 1}});
          visited[ny][nx][bc + 1] = true;
        }
        if (area[ny][nx] == 0 && !visited[ny][nx][bc]) { // 안부수는 경우
          q.push({{nx, ny}, {bc, dist + 1}});
          visited[ny][nx][bc] = true;
        }
      }
    }
  }
  return -1;
}

int main() {
  cin >> H >> W;
  string in;
  for (int i = 1; i <= H; i++) {
    cin >> in;
    for (int j = 1; j <= W; j++) {
      area[i][j] = in[j - 1] - '0';
    }
  }
  cout << bfs();
}
