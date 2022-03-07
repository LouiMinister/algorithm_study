

#include <iostream>
#include <vector>
using namespace std;

class Tree {
private:
  int size;
  vector<int> lc;
  vector<int> rc;

public:
  Tree() { Tree(0); }
  Tree(int size) {
    this->size = size;
    lc.resize(size, -1);
    rc.resize(size, -1);
  }

  void add_node(int n, int lcn, int rcn) {
    if (lcn > 0)
      lc[n] = lcn;
    if (rcn > 0)
      rc[n] = rcn;
  }

  void preorder(int n) {
    cout << (char)(n + 65);
    if (lc[n] != -1) {
      preorder(lc[n]);
    }
    if (rc[n] != -1) {
      preorder(rc[n]);
    }
  }

  void inorder(int n) {
    if (lc[n] != -1) {
      inorder(lc[n]);
    }
    cout << (char)(n + 65);
    if (rc[n] != -1) {
      inorder(rc[n]);
    }
  }

  void postorder(int n) {
    if (lc[n] != -1) {
      postorder(lc[n]);
    }
    if (rc[n] != -1) {
      postorder(rc[n]);
    }
    cout << (char)(n + 65);
  }
};

int main() {
  int size;
  char n, lcn, rcn;

  cin >> size;
  Tree tree(size);
  for (int i = 0; i < size; i++) {
    cin >> n >> lcn >> rcn;
    tree.add_node((n - 65), (lcn - 65), (rcn - 65));
  }
  tree.preorder(0);
  cout << endl;
  tree.inorder(0);
  cout << endl;
  tree.postorder(0);
}
