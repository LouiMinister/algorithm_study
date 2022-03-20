#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;
const int CANDY_CNT_MAX = 50;
const int CANDY_PRICE_MAX = 10000;
const int SUMMAX = 500000;

int N, zeroCnt = 1;
set<int> candyExist;
vector<int> candyCnt;
vector<long long> caseOfSum;
vector<bool> eratos;

void eratostenes(int n) {
  eratos.resize(n + 1, true);
  eratos[0] = false;
  eratos[1] = false;
  for (int i = 2; i * i <= n; i++) {
    if (eratos[i] == true) {
      for (int j = i * 2; j <= n; j += i) {
        eratos[j] = false;
      }
    }
  }
}

int main() {
  cin >> N;
  candyCnt.resize(CANDY_PRICE_MAX + 1, 0);
  for (int i = 1; i <= N; i++) {
    int tmp;
    cin >> tmp;
    candyExist.insert(tmp);
    candyCnt[tmp]++;
  }

  caseOfSum.resize(SUMMAX + 1, 0);
  caseOfSum[0] = candyCnt[0] + 1;
  candyExist.erase(0);
  eratostenes(SUMMAX);

  for (auto candy : candyExist) {
    for (int sum = SUMMAX; sum >= 0; sum--) {
      for (int cnt = 1; cnt <= candyCnt[candy]; cnt++) {
        if (sum - candy * cnt >= 0) {
          caseOfSum[sum] += caseOfSum[sum - candy * cnt];
        }
      }
    }
  }

  long long sumOfPrimes = 0;
  for (int i = 2; i <= SUMMAX; i++) {
    if (eratos[i]) {
      sumOfPrimes += caseOfSum[i];
    }
  }
  cout << sumOfPrimes;
}
