#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int N;
int longestIdx = 1;
vector<int> ary(1, 0); // input
vector<int> cnt;       // 연결된 개수 cnt
vector<int> link;      // 연결 index

int main() {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    int tmp;
    cin >> tmp;
    ary.push_back(tmp);
  }
  cnt.resize(N + 1, 0);
  link.resize(N + 1, 0);

  for (int i = 1; i <= N; i++) {
    int maxi = 0;
    int maxl = -1;
    for (int j = i - 1; j > 0; j--) {
      if (ary[j] < ary[i]) {
        if (maxl < cnt[j]) {
          maxi = j;
          maxl = cnt[j];
        }
      }
    }
    if (maxi > 0) {
      link[i] = maxi;
      cnt[i] = maxl + 1;
      if (cnt[longestIdx] < cnt[i]) {
        longestIdx = i;
      }
    }
  }

  // for (int i = 1; i <= N; i++) {
  //   cout << ary[i] << ' ' << link[i] << ' ' << cnt[i] << endl;
  // }
  // cout << longestIdx << endl;

  cout << cnt[longestIdx] + 1 << endl;
  stack<int> ans;
  int nextIdx = longestIdx;
  while (nextIdx != 0) {
    ans.push(nextIdx);
    nextIdx = link[nextIdx];
  }
  while (!ans.empty()) {
    cout << ary[ans.top()] << ' ';
    ans.pop();
  }
}
