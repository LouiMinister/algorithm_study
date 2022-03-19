#include <iostream>
#include <limits.h>
#include <vector>

using namespace std;

vector<int> ary(1, -1);
vector<vector<int>> dp;
vector<vector<bool>> checked;
int N;
int M;

int sumFromTo(int i, int j) {
  int res = 0;
  for (; i <= j; i++) {
    res += ary[i];
  }
  return res;
}

int recur(int n, int m) {
  if (n <= 0 || m <= 0) {
    return 0;
  }
  if (checked[m][n] == true) {
    return dp[m][n];
  } else {
    int case1 = INT_MIN, case2 = INT_MIN;
    if (n - 1 >= m * 2 - 1) {
      case1 = max(case1, recur(n - 1, m)); // ary[m]을 구간에 포함하지 않을 경우
    }
    for (int k = m * 2 - 1; k <= n;
         k++) { // ary[m]을 구간에 포함할 경우 k는 m*2-1 보단 크거나 같아야함
      if (k - 2 >= (m - 1) * 2 - 1) {
        int val = recur(k - 2, m - 1) + sumFromTo(k, n);
        if (val > case2) {
          case2 = val;
        }
      }
    }
    dp[m][n] = max(case1, case2);
    checked[m][n] = true;
    return dp[m][n];
  }
}

int main() {
  cin >> N >> M;
  for (int i = 1; i <= N; i++) {
    int tmp;
    cin >> tmp;
    ary.push_back(tmp);
  }

  dp.resize(M + 1, vector<int>(N + 1, 0));
  dp[1][1] = ary[1];
  checked.resize(M + 1, vector<bool>(N + 1, false));
  checked[1][1] = true;

  cout << recur(N, M) << endl;
};
