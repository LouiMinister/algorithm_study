#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

vector<vector<int>> img;
int N;

bool isSame(int n, int x, int y) {
  int cache = img[y][x];
  for (int i = y; i < y + n; i++) {
    for (int j = x; j < x + n; j++) {
      if (cache != img[i][j]) {
        return false;
      }
      cache = img[i][j];
    }
  }
  return true;
}

void dnq(int n, int x, int y) {
  if (n == 1 || isSame(n, x, y)) {
    cout << img[y][x];
  } else {
    cout << '(';
    dnq(n / 2, x, y);
    dnq(n / 2, x + n / 2, y);
    dnq(n / 2, x, y + n / 2);
    dnq(n / 2, x + n / 2, y + n / 2);
    cout << ')';
  }
}

int main() {
  // input
  cin >> N;
  img.resize(N + 1, vector<int>(N + 1, -1));
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      scanf("%1d", &img[i][j]);
    }
  }
  // logic
  dnq(N, 1, 1);
}
