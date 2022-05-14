#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int N, M;
int Map[1001][1001];
int BSpace[1123123];
int BTag[1001][1001];
int Res[1001][1001];
int TagIdx = 1;

int DeltaX[] = {1, 0, -1, 0};
int DeltaY[] = {0, 1, 0, -1};

bool isInRange(int x, int y) { return x >= 1 && x <= M && y >= 1 && y <= N; }

int getSpaceSize(int x, int y) {
  if (isInRange(x, y) && Map[y][x] == 0 && BTag[y][x] == 0) {
    int sum = 1;
    BTag[y][x] = TagIdx;
    for (int i = 0; i < 4; i++) {
      sum += getSpaceSize(x + DeltaX[i], y + DeltaY[i]);
    }
    return sum;
  }
  return 0;
}

int main() {
  cin >> N >> M;

  string tmp;
  for (int i = 1; i <= N; i++) {
    cin >> tmp;
    for (int j = 1; j <= M; j++) {
      Map[i][j] = tmp.at(j - 1) - '0';
    }
  }
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      if (Map[i][j] != 1 && BTag[i][j] == 0) {
        BSpace[TagIdx] = getSpaceSize(j, i);
        TagIdx++;
      }
    }
  }

  int sum = 0;
  vector<int> check;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      if (Map[i][j] != 1) {
        cout << 0;
        continue;
      }
      sum = 1;
      for (int k = 0; k < 4; k++) {
        int x = j + DeltaX[k];
        int y = i + DeltaY[k];
        if (!isInRange(x, y) || Map[y][x] == 1)
          continue;
        int nowTag = BTag[y][x];
        if (find(check.begin(), check.end(), nowTag) == check.end()) {
          check.push_back(nowTag);
          sum += BSpace[nowTag];
        }
      }
      check.clear();
      cout << sum % 10;
    }
    cout << '\n';
  }
}
