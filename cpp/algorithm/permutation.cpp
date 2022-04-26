#include <algorithm>
#include <iostream>

using namespace std;

void Permutation(int *a, int n, int m) {
  if (n == m) {
    for (int i = 0; i <= m; i++) {
      cout << a[i] << ' ';
    }
    cout << endl;
  } else {
    for (int i = n; i <= m; i++) {
      swap(a[n], a[i]);
      Permutation(a, n + 1, m);
      swap(a[i], a[n]);
    }
  }
}

int main() {
  int a[] = {1, 2, 3};
  Permutation(a, 0, 2);
}
