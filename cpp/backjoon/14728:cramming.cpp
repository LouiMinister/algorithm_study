#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int TN, BW;
int TW[101];
int TC[101];
int DP[10001];
int main() {
  cin >> TN >> BW;
  for (int i = 1; i <= TN; i++) {
    cin >> TW[i] >> TC[i];
  }
  int res = 0;
  for (int Tj = 1; Tj <= TN; Tj++) {
    for (int Wi = BW; Wi > 0; Wi--) {
      int beforeWeight = Wi - TW[Tj];
      if (beforeWeight >= 0) {
        DP[Wi] = max(DP[Wi], DP[beforeWeight] + TC[Tj]);
      }
    }
  }
  cout << DP[BW];
}
