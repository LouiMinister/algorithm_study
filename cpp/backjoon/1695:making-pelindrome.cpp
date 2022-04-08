#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

int N;
int S[5000];
int DP[5000][5000];

int main() {
  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> S[i];
  }

  for (int j = 0; j < N; j++) {
    for (int i = 0; i < N - j; i++) {
      int l = i;
      int r = i + j;
      if (S[l] == S[r]) {
        DP[l][r] = DP[l + 1][r - 1];
      } else {
        DP[l][r] = min(DP[l + 1][r], DP[l][r - 1]) + 1;
      }
    }
  }

  cout << DP[0][N - 1];
} // 반복 DP

/* 재귀 DP
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

int N;
int S[5000];
int Memo[5000][5000];

int recur(int l, int r) {
  int res;
  if (Memo[l][r] != -1) {
    return Memo[l][r];
  }
  if (l >= r) {
    res = 0;
  } else if (S[l] == S[r]) {
    res = recur(l + 1, r - 1);
  } else {
    res = min(recur(l + 1, r), recur(l, r - 1)) + 1;
  }
  Memo[l][r] = res;
  return res;
}

int main() {
  cin >> N;
  fill_n(&Memo[0][0], 5000 * 5000, -1);
  for (int i = 0; i < N; i++) {
    cin >> S[i];
  }
  cout << recur(0, N - 1);
}


*/
