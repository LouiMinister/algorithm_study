#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int P;
int CN;
int CCost[10001];
int CCnt[1001];
int DP[10001] = {
    1,
};

int main() {
  cin >> P >> CN;
  for (int i = 1; i <= CN; i++) {
    cin >> CCost[i] >> CCnt[i];
  }

  for (int CCostI = 1; CCostI <= CN; CCostI++) { // CCost CCnt의 Idx
    for (int sum = P; sum > 0; sum--) {          // 합
      for (int CCntJ = 1; CCntJ <= CCnt[CCostI];
           CCntJ++) { // 해당 CCost의 Cnt 순회
        int before = sum - CCost[CCostI] * CCntJ;
        if (before >= 0) {
          DP[sum] += DP[sum - CCost[CCostI] * CCntJ];
        }
      }
    }
  }

  cout << DP[P];
}
