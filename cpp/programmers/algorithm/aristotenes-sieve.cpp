#include <iostream>
// #include <algorithm>

using namespace std;

bool *logic(int n) {
  bool primes[n + 1];
  for (int i = 2; i < n + 1; i++) {
    primes[i] = true;
  }
  for (int i = 2; i * i <= n; i++) {
    if (primes[i]) {
      for (int j = i * i; j <= n; j += i) {
        primes[j] = false;
      }
    }
  }
  return primes;
}

int main(int n

) {
  // input 값
  n = 100;
  bool *result = logic(n);

  // 출력
  for (int i = 0; i < n + 1; i++) {
    cout << result[i] << ' ';
  }
}
