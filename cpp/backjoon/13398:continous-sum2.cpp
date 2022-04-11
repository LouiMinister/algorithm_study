#include <algorithm>
#include <iostream>
#include <limits.h>

using namespace std;

int N;
int DP[112345][2];
int ary[112345];
int main() {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    cin >> ary[i];
  }

  DP[1][0] = ary[1];
  int res = DP[1][0];
  if (N >= 3) {
    DP[3][1] = ary[1] + ary[3];
    res = max(res, DP[3][1]);
  }
  for (int i = 2; i <= N; i++) {
    DP[i][0] = max(DP[i - 1][0] + ary[i], ary[i]);
    res = max(res, DP[i][0]);
    if (i >= 4) {
      DP[i][1] = max(DP[i - 1][1] + ary[i], DP[i - 2][0] + ary[i]);
      res = max(res, DP[i][1]);
    }
  }

  cout << res;
}
