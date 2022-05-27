#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <string>
#include <vector>

using namespace std;

int N;
int area[26][26];
int visited[26][26];
vector<int> res;
int cnt;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void bfs() {
  queue<pair<int, int>> q;
  pair<int, int> src;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (visited[i][j] == true || area[i][j] == 0)
        continue;
      src = {j, i};
      q.push(src);
      visited[i][j] = 1;
      int size = 1;
      while (!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();
        for (int k = 0; k < 4; k++) {
          int x = cur.first + dx[k];
          int y = cur.second + dy[k];
          if (x >= 1 && y >= 1 && x <= N && y <= N && visited[y][x] == 0 &&
              area[y][x] == 1) {
            q.push({x, y});
            visited[y][x] = 1;
            size++;
          }
        }
      }
      cnt++;
      res.push_back(size);
    }
  }
  sort(res.begin(), res.end());
}

int main() {
  cin >> N;
  cin.ignore();
  string in;
  for (int i = 1; i <= N; i++) {
    getline(cin, in);
    for (int j = 1; j <= N; j++) {
      area[i][j] = in[j - 1] - '0';
    }
  }
  bfs();
  cout << cnt << '\n';
  for (int v : res) {
    cout << v << '\n';
  }
}
