#include <algorithm>
#include <cmath>
#include <iostream>
#include <stdexcept>

using namespace std;

// Try 1 -> 접근 불가능
// Try 2 -> At1NodeA에서 friend 선언
// Try 3 -> Has a 관계

template <class T> class Chain;
template <class T> class ChainNode {
  friend class Chain<T>;

public:
  ChainNode() { link = 0; }
  ChainNode(T v) : ChainNode() { data = v; }

private:
  T data;
  ChainNode<T> *link;
};

template <class T> class Chain {
private:
  ChainNode<T> *first;
  ChainNode<T> *last;

  ChainNode<T> *locateAt(int n) {
    if (n < -1) {
      throw out_of_range("Out of Range!");
    }
    ChainNode<T> *it = first;
    for (int i = 0; i <= n; i++) {
      it = it->link;
      if (it == 0) // 마지막 주소보다 더 나갔을 경우
        throw out_of_range("Out of Range!");
    }
    return it;
  }

public:
  Chain() {
    ChainNode<T> *dummy = new ChainNode<T>();
    first = dummy;
    last = dummy;
  }

  T at(int n) { // 없을 경우 null 리턴
    ChainNode<T> *adr = locateAt(n);
    return adr->data;
  }

  bool isEmpty() { return first == last; }

  void insertBack(T v) {
    ChainNode<T> *newNode = new ChainNode<T>(v);
    last->link = newNode;
    last = newNode;
  }

  void remove(int i) {
    if (isEmpty()) {
      throw out_of_range("Out of Range!");
    }
    ChainNode<T> *befIAdr = locateAt(i - 1);
    ChainNode<T> *iAdr = (befIAdr->link);
    if (iAdr == last) {
      befIAdr->link = 0;
      last = befIAdr;
      delete iAdr;
    } else {
      befIAdr->link = iAdr->link;
      delete iAdr;
    }
  }

  void print() {
    ChainNode<T> *i = first->link;
    while (i != 0) {
      cout << i->data << ' ';
      i = i->link;
    }
    cout << '\n';
  }
};

int main() {
  // Chain<int> chain;
  // chain.insertBack(1);
  // chain.insertBack(2);
  // chain.insertBack(3);
  // chain.print();
  // chain.remove(1);
  // chain.print();
  // chain.remove(0);
  // chain.print();
  // chain.remove(0);
  // chain.print();
  // chain.remove(0);
  // int i = 3;
  // cout << chain.at(2);
}
