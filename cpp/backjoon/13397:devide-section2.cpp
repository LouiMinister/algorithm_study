#include <algorithm>
#include <cmath>
#include <iostream>
#include <utility>

using namespace std;

int ary[5001];
int N, M;

bool isPossible(int res) {
  int cnt = M;
  int minV = ary[1];
  int maxV = ary[1];
  for (int i = 1; i <= N; i++) {
    maxV = max(maxV, ary[i]);
    minV = min(minV, ary[i]);
    if (maxV - minV > res) { // 초과 시 i까지를 구간으로 함
      cnt--;
      minV = ary[i];
      maxV = ary[i];
    }
  }
  return cnt > 0;
}

int main() {
  cin >> N >> M;
  for (int i = 1; i <= N; i++) {
    cin >> ary[i];
  }

  int left = 0;
  int right = 10000;
  int mid;
  int res = 1;
  while (left <= right) { // 값이 더 작아져도 되는 경우
    mid = (left + right) / 2;
    if (isPossible(mid)) {
      res = mid;
      right = mid - 1;
    } else { // 값이 더 커져야만 하는 경우
      left = mid + 1;
    }
  }
  cout << res;
}
