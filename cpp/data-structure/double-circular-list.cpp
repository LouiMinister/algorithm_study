#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

template <class T> class CircularDList {
private:
  class Node {
  public:
    T data;
    Node *left;
    Node *right;
    Node() {
      left = 0;
      right = 0;
    }
    Node(T v) : Node() { data = v; }
  };
  Node *first;

public:
  CircularDList() { first = 0; }

  void insert_back(T v) {
    Node *newNode = new Node(v);
    if (first == 0) {
      first = newNode;
      newNode->left = newNode;
      newNode->right = newNode;
    } else {
      newNode->right = first->right;
      newNode->left = first;
      first->right = newNode;
      newNode->right->left = newNode;
      first = newNode;
    }
  }

  void print() {
    Node *adrI = first;
    while (true) {
      cout << adrI->data << endl;
      if (adrI->left == first) {
        break;
      }
      adrI = adrI->left;
    }
  }

  void print2() {
    Node *adrI = first;
    while (true) {
      if (adrI->left == first) {
        break;
      }
      adrI = adrI->left;
    }
    while (true) {
      cout << adrI->data << endl;
      if (adrI->right == first->right) {
        break;
      }
      adrI = adrI->right;
    }
  }
};

int main() {
  CircularDList<int> cdlist;

  cdlist.insert_back(1);
  cdlist.insert_back(2);
  cdlist.insert_back(3);
  cdlist.print2();
}
