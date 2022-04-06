#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int N, r, c;
int main() {
  cin >> N >> r >> c;
  int res = 0;
  long long Ns = pow(2, N - 1);
  for (int i = 1; i <= N; i++) {
    bool xDire = false;
    bool yDire = false;
    if (c / Ns >= 1) {
      res += Ns * Ns;
      c -= Ns;
    }
    if (r / Ns >= 1) {
      res += Ns * Ns * 2;
      r -= Ns;
    }

    Ns /= 2;
  }
  cout << res;
}
