#include <algorithm>
#include <cmath>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int CN;
int VN;
int FN;
int DP[301];
vector<vector<pair<int, int>>> F;
int main() {
  cin >> CN >> VN >> FN;
  F.resize(301, vector<pair<int, int>>());

  int a, b, score;
  for (int i = 1; i <= FN; i++) {
    cin >> a >> b >> score;
    if (a < b) {
      F[b].push_back(pair<int, int>(a, score));
    }
  }

  fill_n(DP, 301, -1);
  DP[1] = 0;
  for (int Vi = 1; Vi <= VN - 1; Vi++) { // 방문한 횟수 순회
    for (int Ci = CN; Ci > 1; Ci--) { // 도시 순회, 뒤에서 순회해야 참조한 값이
                                      // 같은 라운드일 때 바뀌지 않음

      vector<pair<int, int>>::iterator Fi;
      for (Fi = F[Ci].begin(); Fi != F[Ci].end(); Fi++) { // bound check
        int beforeC = (*Fi).first;
        int score = (*Fi).second;
        if (DP[beforeC] != -1) {
          DP[Ci] = max(DP[Ci],
                       DP[beforeC] + score); // 현재 도시의 점수는 비행기 시작
                                             // 도시의 점수 + 기내식 점수
        }
      }
    }
  }

  cout << DP[CN] << endl;
}
