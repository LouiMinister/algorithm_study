#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int alpha[26] = {
      0,
  };
  string result = "";
  string line;
  getline(cin, line);

  for (int i = 0; i < line.size(); i++) {
    alpha[line[i] - 'A'] += 1;
  }
  int oddIdx = -1;
  for (int i = 0; i < 26; i++) {
    if (alpha[i] % 2 == 1) {
      if (oddIdx == -1 && line.size() % 2 == 1) {
        oddIdx = i;
      } else {
        cout << "I'm Sorry Hansoo";
        return 0;
      }
    }
  }

  if (oddIdx != -1) {
    result = oddIdx + 'A';
  }
  for (int i = 25; i >= 0; i--) {
    for (int j = 1; j <= alpha[i] / 2; j++) {
      result = (char)('A' + i) + result + (char)('A' + i);
    }
  }
  cout << result;
}
