#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int aArea[1501][1501];
int aSum[1501][1501];
int bArea[1501][1501];
int bSum[1501][1501];
int width;
int height;
int DP[1501][1501];

int main() {
  cin >> height >> width;

  for (int i = 1; i <= height; i++) {
    for (int j = 1; j <= width; j++) {
      string input;
      cin >> input;
      if (input[0] == 'A') { // AN
        aArea[i][j] = stoi(input.substr(1, input.size()));
      } else { // BN
        bArea[i][j] = stoi(input.substr(1, input.size()));
      }
      if (j > 1) {
        aSum[i][j] = aSum[i][j - 1] + aArea[i][j - 1]; // set aSum
      }
    }
  }

  for (int i = 1; i <= width; i++) {
    for (int j = 2; j <= height; j++) {
      bSum[j][i] = bSum[j - 1][i] + bArea[j - 1][i]; // set bSum
    }
  }

  DP[1][1] = 0;
  for (int i = 2; i <= height; i++) {
    for (int j = 2; j <= width; j++) {
      DP[i][j] = max(DP[i][j], DP[i - 1][j - 1] + aSum[i][j] + bSum[i][j]);
      DP[i][j] = max(DP[i][j], DP[i][j - 1] + bSum[i][j]);
      DP[i][j] = max(DP[i][j], DP[i - 1][j] + aSum[i][j]);
    }
  }

  cout << DP[height][width];
}
