#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>

using namespace std;

int W, H;
int area[101][101];
int contact[101][101];
bool visited[101][101];
int leftCheese;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

void bfs(int x, int y) {
  // contact, visited 초기화
  queue<pair<int, int>> q;
  q.push({x, y});
  visited[y][x] = true;

  while (!q.empty()) {
    int nowX = q.front().first;
    int nowY = q.front().second;
    q.pop();
    for (int i = 0; i < 4; i++) {
      int toX = nowX + dx[i];
      int toY = nowY + dy[i];
      if (toX > 0 && toY > 0 && toX <= W && toY <= H && !visited[toY][toX] &&
          area[toY][toX] == 0) {
        visited[toY][toX] = true;
        q.push({toX, toY});
        for (int j = 0; j < 4; j++) {
          if (area[toY + dy[j]][toX + dx[j]] == 1)
            contact[toY + dy[j]][toX + dx[j]]++;
        }
      }
    }
  }

  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      if (contact[i][j] >= 2 && area[i][j] == 1) {
        area[i][j] = 0;
        leftCheese--;
      }
      contact[i][j] = 0; // 초기화
      visited[i][j] = false;
    }
  }
}

int main() {
  cin >> H >> W;
  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      cin >> area[i][j];
      if (area[i][j] == 1) {
        leftCheese += 1;
      }
    }
  }

  int res = 0;
  while (leftCheese > 0) {
    bfs(1, 1);
    res++;
  }
  cout << res;
}
