#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int N;
int main() {

  cin >> N;

  int midLen = 3;
  int sideLen = 0;

  while (N > midLen + sideLen * 2) {
    sideLen = sideLen * 2 + midLen;
    midLen += 1;
  }
  while (true) {
    if (N <= sideLen) { // 왼쪽 side에 N이 포함인 경우
      midLen -= 1;
      sideLen = (sideLen - midLen) / 2;
    } else if (N <= sideLen + midLen) { // mideLen에 포함인 경우
      if (N - sideLen == 1) {
        cout << 'm';
      } else {
        cout << 'o';
      }
      return 0;
    } else { // 오른쪽 side에 N이 포함인 경우
      N -= (sideLen + midLen);
      midLen -= 1;
      sideLen = (sideLen - midLen) / 2;
    }
  }
}
