#include <iostream>
#include <vector>

using namespace std;

bool *aristotenes(int n) {
  bool *primes = new bool[n + 1]();
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
const bool *primes = aristotenes(1000);

vector<int> factorization(int n) {
  vector<int> result;
  int divider = 2;
  while (divider <= n) {
    cout << n << ':' << divider << endl;
    if (primes[divider] == true) {
      while (n % divider == 0) {
        n = n / divider;
        result.push_back(divider);
      }
    }
    divider++;
  }
  return result;
}

int main(void) {
  // input 값
  int n = 100;
  vector<int> result = factorization(n);

  // 출력
  for (int i = 0; i < result.size(); i++) {
    cout << result[i] << ' ';
  }
}
