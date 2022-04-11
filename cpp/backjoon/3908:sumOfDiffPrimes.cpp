#include <algorithm>
#include <cmath>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int N;
vector<pair<int, int>> input;
int DP[1123][15];
bool isPrime[1121];
vector<int> primeAry;

void eratosF() {
  int n = 1120;
  fill_n(isPrime, 1121, 1);
  isPrime[0] = false;
  isPrime[1] = false;

  for (int i = 2; i * i <= n; i++) {
    if (isPrime[i]) {
      for (int j = i * i; j <= n; j += i) {
        isPrime[j] = false;
      }
    }
  }
  for (int i = 2; i <= n; i++) {
    if (isPrime[i]) {
      primeAry.push_back(i);
    }
  }
}

int main() {
  cin >> N;
  int tmp1, tmp2;
  for (int i = 0; i < N; i++) {
    cin >> tmp1 >> tmp2;
    input.push_back(pair<int, int>(tmp1, tmp2));
  }
  eratosF();

  DP[0][0] = 1; // DP[n][k] => 값 n을 k개의 소수로 만들 수 있는 개수
  for (int prime : primeAry) {              // 소수들
    for (int i = 1120; i >= prime; i--) {   // 덧셈의 합
      for (int cnt = 1; cnt <= 14; cnt++) { // 더한 갯수
        if (i - prime >= 0) {
          DP[i][cnt] += DP[i - prime][cnt - 1];
        }
      }
    }
  }

  for (int i = 0; i < N; i++) {
    pair<int, int> val = input[i];
    cout << DP[val.first][val.second] << endl;
  }
}
