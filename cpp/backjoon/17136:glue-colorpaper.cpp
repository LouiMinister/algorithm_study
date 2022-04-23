#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int Area[11][11];
int leftP[6] = {0, 5, 5, 5, 5, 5};
int res = 987654321;

pair<int, int> nextPos() {
  for (int i = 1; i <= 10; i++) {
    for (int j = 1; j <= 10; j++) {
      if (Area[i][j] == 1) {
        return make_pair(j, i);
      }
    }
  }
  return make_pair(-1, -1);
}

bool isAnswer() {
  for (int i = 1; i <= 10; i++) {
    for (int j = 1; j <= 10; j++) {
      if (Area[i][j] == 1)
        return false;
    }
  }
  return true;
}

void fillArea(int x, int y, int size, int num) {
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      Area[y + i][x + j] = num;
    }
  }
}

bool canGlue(int x, int y, int size) {
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      if (Area[y + i][x + j] == 0) {
        return false;
      }
    }
  }
  return true;
}

void BFS(int cnt) {
  if (isAnswer()) {
    res = min(res, cnt);
    return;
  }
  pair<int, int> nextCoord = nextPos();
  if (nextCoord.first == -1)
    return;
  for (int i = 5; i >= 1; i--) {
    if (leftP[i] > 0 && canGlue(nextCoord.first, nextCoord.second, i)) {
      leftP[i]--;
      fillArea(nextCoord.first, nextCoord.second, i, 0);
      BFS(cnt + 1);
      leftP[i]++;
      fillArea(nextCoord.first, nextCoord.second, i, 1);
    }
  }
}

int main() {
  for (int i = 1; i <= 10; i++) {
    for (int j = 1; j <= 10; j++) {
      cin >> Area[i][j];
    }
  }

  BFS(0);
  if (res == 987654321) {
    res = -1;
  }
  cout << res;
}
