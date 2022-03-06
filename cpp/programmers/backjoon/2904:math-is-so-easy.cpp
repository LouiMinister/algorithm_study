#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int const MAX = 1000000;
static bool *primes;

void ertostenes() {
  int n = MAX;
  bool *result = new bool[n + 1]();
  for (int i = 2; i < n + 1; i++) {
    result[i] = true;
  }
  for (int i = 2; i * i <= n; i++) {
    if (result[i]) {
      for (int j = i * i; j <= n; j += i) {
        result[j] = false;
      }
    }
  }
  primes = result;
}

map<int, int> factorization(int num) {
  map<int, int> result;
  for (int divider = 2; divider <= num && num != 1; divider++) {
    if (primes[divider] == true) {
      while (num % divider == 0) {
        num = num / divider;
        result[divider] += 1;
      }
    }
  }
  return result;
}

int main() {
  // input
  int paperSize;
  cin >> paperSize;
  vector<int> papers(paperSize);
  for (int i = 0; i < paperSize; i++) {
    cin >> papers.at(i);
  }

  ertostenes();
  double result[2] = {1, 0};

  vector<map<int, int>> factorizedPapers(paperSize);
  map<int, int> reducedFactorizedPapers;
  for (int i = 0; i < paperSize; i++) {
    factorizedPapers[i] = factorization(papers[i]);
    for (map<int, int>::iterator iter = factorizedPapers[i].begin();
         iter != factorizedPapers[i].end(); iter++) {
      reducedFactorizedPapers[iter->first] += iter->second;
    }
  }

  map<int, int> reducedAndDividedFactorizedPapers;
  for (map<int, int>::iterator iter = reducedFactorizedPapers.begin();
       iter != reducedFactorizedPapers.end(); iter++) {
    int dividedExp = floor(iter->second / paperSize);
    reducedAndDividedFactorizedPapers[iter->first] = dividedExp;
    result[0] *= pow(iter->first, dividedExp);
  }

  for (int i = 0; i < paperSize; i++) {
    for (map<int, int>::iterator iter =
             reducedAndDividedFactorizedPapers.begin();
         iter != reducedAndDividedFactorizedPapers.end(); iter++) {
      int diff = iter->second - factorizedPapers[i][iter->first];
      if (diff > 0) {
        result[1] += diff;
      }
    }
  }
  // output
  cout << result[0] << " " << result[1] << "\n";
}
