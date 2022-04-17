#include <iostream>
#include <set>
#include <string>

using namespace std;

int cnt = 0;
int N, M;
set<string> s;
set<string> res;

int main() {
  cin >> N >> M;
  string tmp;

  for (int i = 1; i <= N; i++) {
    cin >> tmp;
    s.insert(tmp);
  }
  for (int i = 1; i <= M; i++) {
    cin >> tmp;
    if (s.find(tmp) != s.end()) {
      cnt++;
      res.insert(tmp);
    }
  }

  cout << cnt << endl;
  for (string str : res) {
    cout << str << endl;
  }
}
