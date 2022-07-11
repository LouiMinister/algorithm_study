#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int L, C;
vector<char> ch;

bool check(vector<int> v, int lastI) {
  if (v.size() == L) {
    int mCnt = 0;
    for (int c : v) {
      if (ch[c] == 'a' || ch[c] == 'e' || ch[c] == 'i' || ch[c] == 'o' ||
          ch[c] == 'u')
        mCnt++;
    }
    return mCnt > 0 && (v.size() - mCnt) >= 2;
  }
  return true;
}

void dfs(vector<int> v, int lastI) {
  if (v.size() == L) {
    for (int i = 0; i < v.size(); i++) {
      cout << ch[v[i]];
    }
    cout << '\n';
    return;
  }

  for (int i = lastI + 1; i < C; i++) {
    v.push_back(i);
    if (check(v, i)) {
      dfs(v, i);
    }
    v.pop_back();
  }
}

int main() {
  cin >> L >> C;
  char c;
  for (int i = 0; i < C; i++) {
    cin >> c;
    ch.push_back(c);
  }
  sort(ch.begin(), ch.end());
  vector<int> v;
  dfs(v, -1);
}
