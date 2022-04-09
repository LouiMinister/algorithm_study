#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int W, H;
int DH[501][501];
int Memo[501][501];
int Dx[] = {1, -1, 0, 0};
int Dy[] = {0, 0, -1, 1};

bool inField(int x, int y) { return x >= 1 && y >= 1 && x <= W && y <= H; }

int DP(int x, int y) {
  if (Memo[x][y] != -1) {
    return Memo[x][y];
  }
  int res = 0;
  for (int i = 0; i < 4; i++) {
    int befX = x + Dx[i];
    int befY = y + Dy[i];
    if (DH[befY][befX] > DH[y][x] && inField(befX, befY)) {
      res += DP(befX, befY);
    }
  }
  Memo[x][y] = res;
  return res;
}

int main() {
  cin >> H >> W;
  for (int Hi = 1; Hi <= H; Hi++) {
    for (int Wi = 1; Wi <= W; Wi++) {
      cin >> DH[Hi][Wi];
    }
  }
  fill_n(&Memo[0][0], 501 * 501, -1);
  Memo[1][1] = 1;
  cout << DP(W, H);
}
