#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int N, K;
  cin >> N >> K;
  vector<int> res;
  vector<int> C = {0};
  for (int i = 1; i <= N; i++) {
    C.push_back(i);
  }
  int accK = K;

  while (C.size() != 1) {
    while (C.size() - 1 < accK) {
      accK -= C.size() - 1;
    }
    res.push_back(C[accK]);
    C.erase(C.begin() + accK);
    accK += K - 1;
  }

  cout << '<' << res[0];
  for (int i = 1; i < N; i++) {
    cout << ", " << res[i];
  }
  cout << '>';
}
