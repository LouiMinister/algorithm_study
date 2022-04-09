#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

short H[2200][2200];
int N;
int E = 0;
int sumsum[3];
const short IMPERFACT = -2;

int dq(int x, int y, int N) {
  if (N == 1) {
    return H[y][x];
  }
  int sum[3] = {0}; // -1 0 1 순서

  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      int val = dq(x + j * N / 3, y + i * N / 3, N / 3);
      if (val != IMPERFACT) {
        sum[val + 1] += 1;
      }
    }
  }

  for (int i = 0; i < 3; i++) {
    if (sum[i] == 9) { // 완전한 종이
      return i - 1;
    }
  }
  for (int i = 0; i < 3; i++) { // 불완전한 종이인경우
    sumsum[i] += sum[i];
  }
  return IMPERFACT;
}

int main() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> H[i][j];
    }
  }
  int tmp = N;
  while (tmp != 1) {
    tmp /= 3;
    E++;
  }
  int res = dq(0, 0, N);
  if (res != IMPERFACT) {
    sumsum[res + 1] += 1;
  }
  for (int val : sumsum) {
    cout << val << endl;
  }
}
