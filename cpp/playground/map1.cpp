#include <iostream>
#include <map>

using namespace std;

class comp {
public:
  bool operator()(const int &lhs, const int &rhs) const { return lhs > rhs; }
};

int main() {
  map<int, int> m1;
  m1[1] = 2;                  // {1,2}
  m1[1] = 3;                  // {1,3}
  m1.insert(make_pair(1, 4)); // {1,3}
  m1.insert({1, 5});          // {1,3}

  // for (auto p : m1) {
  //   cout << p.first << ' ' << p.second << endl;
  // }

  map<int, int>::iterator i = m1.find(1);
  cout << (*i).first << ' ' << (*i).second << endl;
  cout << m1.count(1) << endl;
}
