#include <iostream>
#include <set>

using namespace std;

int N;
class comp {
public:
  bool operator()(const string &lhs, const string &rhs) const {
    if (lhs.length() == rhs.length()) {
      return lhs < rhs;
    } else {
      return lhs.length() < rhs.length();
    }
  }
};

int main() {
  cin >> N;
  set<string, comp> s;
  string tmp;
  for (int i = 1; i <= N; i++) {
    cin >> tmp;
    s.insert(tmp);
  }

  for (string str : s) {
    cout << str << endl;
  }
}
