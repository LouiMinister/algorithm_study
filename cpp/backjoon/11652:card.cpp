#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

int N;
int maxCnt = 0;
map<long, int> m;
int main() {
  cin >> N;
  long tmp;
  for (int i = 1; i <= N; i++) {
    cin >> tmp;
    if (m.count(tmp) == 0) {
      m.insert({tmp, 1});
    } else {
      m[tmp]++;
    }
    maxCnt = max(maxCnt, m[tmp]);
  }

  for (pair<long, int> p : m) {
    if (p.second == maxCnt) {
      cout << p.first << endl;
      return 0;
    }
  }
}
