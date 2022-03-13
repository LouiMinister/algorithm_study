#include <iostream>
#include <limits.h>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

vector<int> marbles = {-1};
int groupsCnt;

bool check(int sumMax) {
  int sum = 0, cnt = 1;
  for (int i = 1; i < marbles.size(); i++) {
    if (sumMax < sum + marbles[i]) {
      sum = marbles[i];
      cnt++;
    } else {
      sum += marbles[i];
    }
  }
  return cnt <= groupsCnt;
}

void print(int groupMaxCnt, int sumMax) {
  int i, sum = 0, marbleCnt = 0;
  for (int i = 1; i < marbles.size(); i++) {
    sum += marbles[i];
    if (sum > sumMax) {
      sum = marbles[i];
      groupMaxCnt--;
      cout << marbleCnt << " ";
      marbleCnt = 0;
    }
    marbleCnt++;
    if (marbles.size() - i == groupMaxCnt)
      break;
  }

  while (groupMaxCnt--) {
    cout << marbleCnt << " ";
    marbleCnt = 1;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int marbleCnt;
  int lo = 0;
  int hi = 0;
  // input
  cin >> marbleCnt >> groupsCnt;
  for (int i = 1; i <= marbleCnt; i++) {
    int val;
    cin >> val;
    marbles.push_back(val);
    hi += val;
    lo = max(lo, val);
  }

  while (lo < hi) {
    int mid = (lo + hi) / 2;
    int result;
    if (check(mid)) {
      hi = mid;
    } else {
      lo = mid + 1;
    }
  }
  cout << lo << endl;
  print(groupsCnt, lo);
}
