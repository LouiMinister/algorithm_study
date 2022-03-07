
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class Tree {

public:
  vector<int> ln;
  vector<int> rn;
  vector<int> pn;
  int root;
  vector<int> xCoord;
  vector<int> yCoord;
  int xIt = 1;

  Tree(int size) {
    pn.resize(size + 1, -1);
    ln.resize(size + 1, -1);
    rn.resize(size + 1, -1);
    xCoord.resize(size + 1, -1);
    yCoord.resize(size + 1, -1);
  }
  void addNode(int n, int lnv, int rnv) {
    if (lnv != -1) {
      ln[n] = lnv;
      pn[lnv] = n;
    }
    if (rnv != -1) {
      rn[n] = rnv;
      pn[rnv] = n;
    }
  }
  int getRoot(int n) {
    while (pn[n] != -1) {
      n = pn[n];
    }
    return n;
  }
  void setXCoord(int root) {
    if (ln[root] != -1)
      setXCoord(ln[root]);
    xCoord[root] = xIt;
    xIt++;
    if (rn[root] != -1)
      setXCoord(rn[root]);
  }
  void setYCoord(int root) {
    queue<int> q;
    q.push(root);
    yCoord[root] = 1;

    vector<vector<int>> columnOnLevel;
    columnOnLevel.resize(xCoord.size() + 1, vector<int>());
    columnOnLevel[root].push_back(xCoord[root]);
    while (!q.empty()) {
      int n = q.front();
      q.pop();
      if (ln[n] != -1) {
        q.push(ln[n]);
        yCoord[ln[n]] = yCoord[n] + 1;
        columnOnLevel[yCoord[n] + 1].push_back(xCoord[ln[n]]);
      }
      if (rn[n] != -1) {
        q.push(rn[n]);
        yCoord[rn[n]] = yCoord[n] + 1;
        columnOnLevel[yCoord[n] + 1].push_back(xCoord[rn[n]]);
      }
    }

    int maxY = 1;
    int maxWidth = 1;
    for (int i = 2; !columnOnLevel[i].empty(); i++) {
      int width = columnOnLevel[i].back() - columnOnLevel[i].front() + 1;
      if (columnOnLevel[i].back() - columnOnLevel[i].front() + 1 > maxWidth) {
        maxWidth = width;
        maxY = i;
      }
    }
    cout << maxY << " " << maxWidth << endl;
  }
};

int main() {
  int size;
  cin >> size;
  Tree tree(size);
  for (int i = 0; i < size; i++) {
    int n, lnv, rnv;
    cin >> n >> lnv >> rnv;
    tree.addNode(n, lnv, rnv);
  }
  int root = tree.getRoot(1);
  tree.setXCoord(root);
  tree.setYCoord(root);
}
