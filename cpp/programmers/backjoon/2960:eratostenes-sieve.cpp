
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n, k;
  cin >> n;
  cin >> k;

  vector<bool> ary(n + 1);
  for (int i = 2; i < n + 1; i++) {
    ary[i] = true;
  }

  for (int p = 2; p <= n; p++) {
    for (int i = p; i <= n; i += p) {
      if (ary[i]) {
        ary[i] = false;
        k--;
        if (k == 0) {
          cout << i;
          return 0;
        }
      }
    }
  }
}
