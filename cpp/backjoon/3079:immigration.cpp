#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

long long T[100001];
long long F;
long long S;

long long leftTime(long long maxTime) {
  long long sum = 0;
  for (int i = 0; i < S; i++) {
    sum += (long long)(maxTime / T[i]);
  }
  return sum - F;
}

int main() {
  cin >> S >> F;
  long long left = 0;
  long long right = 0;
  long long mid = 0;

  for (int i = 0; i < S; i++) {
    cin >> T[i];
    right = max(right, T[i]);
  }
  right *= F;
  long long ans = right;

  while (left <= right) {
    mid = (left + right) / 2;
    long long sum = 0;
    for (int i = 0; i < S; i++) {
      sum += mid / T[i];
    }
    if (sum >= F) { // mid가 충분한 경우
      right = mid - 1;
      ans = min(mid, ans);
    } else { // mid가 모자른 경우
      left = mid + 1;
    }
  }
  cout << ans;
  return 0;
}
