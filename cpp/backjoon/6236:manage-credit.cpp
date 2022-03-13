#include <algorithm>
#include <iostream>
#include <limits.h>
#include <vector>

using namespace std;
vector<int> outComes;
int goalCnt;

int check(int withdraw) {
  int credit = 0;
  int cnt = 0;
  for (int i = 0; i < outComes.size(); i++) {
    if (credit < outComes[i]) {
      credit = withdraw;
      cnt++;
    }
    credit -= outComes[i];
  }
  return cnt <= goalCnt;
}

int main() {
  int day;
  int lo = 0;
  int hi = 0;
  // input
  cin >> day >> goalCnt;
  for (int i = 0; i < day; i++) {
    int val;
    cin >> val;
    outComes.push_back(val);
    lo = max(lo, val);
    hi += val;
  }

  while (lo < hi) {
    // cout << lo << ':' << hi << endl;
    int mid = (lo + hi) / 2;
    int result;
    if (check(mid)) {
      hi = mid;
    } else {
      lo = mid + 1;
    }
  }
  cout << lo << endl;
}
