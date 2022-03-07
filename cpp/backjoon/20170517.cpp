#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

class Star {
public:
  vector<vector<bool>> paper;
  int height;

  Star(int height) {
    this->height = height;
    paper.resize(height + 1, vector<bool>(height * 2, false));
    draw(height, height, 1);
  }

  void draw(int h, int x, int y) {
    if (h == 3) {
      paper[y][x] = true;
      paper[y + 1][x - 1] = true;
      paper[y + 1][x + 1] = true;
      for (int i = -2; i <= 2; i++) {
        paper[y + 2][x + i] = true;
      }
      return;
    }
    draw(h / 2, x - h / 2, y + h / 2);
    draw(h / 2, x + h / 2, y + h / 2);
    draw(h / 2, x, y);
  }

  void print() {
    for (int i = 1; i < height + 1; i++) {
      for (int j = 1; j < height * 2; j++) {
        if (paper[i][j]) {
          cout << '*';
        } else {
          cout << ' ';
        }
      }
      cout << endl;
    }
  }
};

int main() {
  int N;
  cin >> N;
  Star star(N);
  star.print();
}
