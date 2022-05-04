#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;
/* dummynode 없는 경우
template <class T> class CircularList {
private:
  class Node {
  public:
    T data;
    Node *link;
    Node() { link = 0; }
    Node(T v) : Node() { data = v; }
  };
  Node *last;

public:
  CircularList() { last = 0; }

  void insert_back(T v) {
    Node *newNode = new Node(v);

    if (last == 0) {
      last = newNode;
      newNode->link = newNode;
    } else {
      newNode->link = last->link;
      last->link = newNode;
      last = newNode;
    }
  }

  void print() {
    Node *adrI = last;
    while (adrI = adrI->link, adrI != last->link) {
      cout << adrI->data << endl;
    }
  }
};
*/

template <class T> class CircularList {
private:
  class Node {
  public:
    T data;
    Node *link;
    Node() { link = 0; }
    Node(T v) : Node() { data = v; }
  };
  Node *last;

public:
  CircularList() {
    Node *dummyNode = new Node(0);
    dummyNode->link = dummyNode;
    last = dummyNode;
  }

  void insert_back(T v) {
    Node *newNode = new Node(v);
    newNode->link = last->link;
    last->link = newNode;
    last = newNode;
  }

  void print() {
    Node *adrI = last->link;
    while (adrI = adrI->link, adrI != last->link) {
      cout << adrI->data << endl;
    }
  }
};

int main() {
  CircularList<int> cl1;
  cl1.insert_back(1);
  cl1.insert_back(2);
  cl1.insert_back(3);
  cl1.insert_back(4);
  cl1.insert_back(5);
  cl1.insert_back(6);
  cl1.print();
}
