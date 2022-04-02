#include <algorithm>
#include <iostream>

using namespace std;

int width;
int height;
int arcadeCnt;
int arcades[51][51]; // 0: 오락실X, n: n번째 오락실
int DP[51][51][51]
      [51]; // 총 방문 오락실 개수, y좌표, x좌표, 최근방문 오락실역 : 경우의수
int main() {
  // input
  cin >> width >> height >> arcadeCnt;
  int input1, input2;
  for (int i = 1; i <= arcadeCnt; i++) {
    cin >> input1 >> input2;
    arcades[input2][input1] = i;
  }

  // for (int i = 1; i <= height; i++) {
  //   for (int j = 1; j <= width; j++) {
  //     cout << arcades[i][j] << ' ';
  //   }
  //   cout << endl;
  // }
  int arcadesAtStart = arcades[1][1];
  if (arcadesAtStart == 0) {
    DP[0][1][1][0] = 1;
  } else {
    DP[1][1][1][arcadesAtStart] = 1;
  }

  for (int aCnt = 0; aCnt <= arcadeCnt; aCnt++) { // 총 방문한 오락실 수
    int a = 3;
    for (int i = 1; i <= height; i++) {
      for (int j = 1; j <= width; j++) {
        if (i == 1 && j == 1)
          continue;
        int nowArcade = arcades[i][j];

        for (int aNum = 0; aNum <= arcadeCnt; aNum++) { // 최근방문 번호
          if (nowArcade == 0) { // Area(j,i)가 오락실이 아닌경우
            DP[aCnt][i][j][aNum] +=
                (DP[aCnt][i - 1][j][aNum] + DP[aCnt][i][j - 1][aNum]) % 1000007;
          } else {                  // Area(j,i)가 오락실인 경우
            if (aNum < nowArcade) { // 최근 방문 오락실번호 < 현재오락실번호
              if (aCnt > 0) {
                DP[aCnt][i][j][nowArcade] += (DP[aCnt - 1][i - 1][j][aNum] +
                                              DP[aCnt - 1][i][j - 1][aNum]) %
                                             1000007;
              }
            } else {
              break;
            }
          }
        }
      }
    }
  }

  for (int aCnt = 0; aCnt <= arcadeCnt; aCnt++) {
    int res = 0;
    for (int aNum = 0; aNum <= arcadeCnt; aNum++) {
      res = (res + DP[aCnt][height][width][aNum]) % 1000007;
    }
    cout << res << ' ';
  }

} // 출력할떄 1,000,007로 나누기
