#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>

using namespace std;

int N;
int area[101][101];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int safeArea(int rain) {
  int res = 0;
  bool visited[101][101];
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (area[i][j] <= rain) {
        visited[i][j] = true;
      } else {
        visited[i][j] = false;
      }
    }
  }

  queue<pair<int, int>> q;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (visited[i][j])
        continue;
      q.push({j, i});
      while (!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();
        for (int k = 0; k < 4; k++) {
          int x = cur.first + dx[k];
          int y = cur.second + dy[k];
          if (x >= 1 && y >= 1 && x <= N && y <= N && visited[y][x] == false) {
            q.push({x, y});
            visited[y][x] = true;
          }
        }
      }
      res++;
    }
  }
  return res;
}

int main() {
  cin >> N;
  int maxHeight = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      cin >> area[i][j];
      maxHeight = max(maxHeight, area[i][j]);
    }
  }

  int res = 1;
  for (int i = 1; i <= maxHeight; i++) {
    res = max(res, safeArea(i));
  }
  cout << res;
}
