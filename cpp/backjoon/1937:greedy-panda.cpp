#include <algorithm>
#include <iostream>

using namespace std;

int N;
int Area[501][501];
int Memo[501][501];
int Dx[4] = {0, 0, -1, 1};
int Dy[4] = {-1, 1, 0, 0};

int DP(int x, int y) {
  if (Memo[y][x] != 0) {
    return Memo[y][x];
  }
  int res = 1;
  for (int i = 0; i < 4; i++) {
    int Sx = x + Dx[i];
    int Sy = y + Dy[i];
    if (Sx >= 1 && Sx <= N && Sy >= 1 && Sy <= N) {
      if (Area[Sy][Sx] < Area[y][x]) {
        res = max(res, DP(Sx, Sy) + 1);
      }
    }
  }
  Memo[y][x] = res;
  return res;
}

int main() {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      cin >> Area[i][j];
    }
  }

  int maxV = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      maxV = max(maxV, DP(i, j));
    }
  }
  cout << maxV;
}
