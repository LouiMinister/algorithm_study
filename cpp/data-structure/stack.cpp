#include <iostream>

using namespace std;

template <typename T> class Stack {
private:
  T *stack;
  int top;
  int capacity;

  void doubleCapacity() {
    T *newStack = new T[capacity * 2];
    copy(stack, stack + capacity, newStack);
    delete stack;
    stack = newStack;
    capacity *= 2;
  }

public:
  Stack(int stackCapacity) : capacity(stackCapacity) {
    if (capacity < 1) {
      throw "Stack capacity must be > 0";
    }
    stack = new T[capacity];
    top = -1;
  }
  ~Stack() { delete stack; }

  void push(T v) {
    if (top + 1 == capacity) {
      doubleCapacity();
    }
    top++;
    stack[top] = v;
  }

  void pop() { top--; }

  T peek() { return stack[top]; }

  void print() {
    for (int i = 0; i < capacity; i++) {
      cout << stack[i] << endl;
    }
  }
};

int main() {
  Stack<int> s(3);
  s.push(1);
  s.push(2);
  s.push(3);
  s.print();
  cout << endl;
  s.push(4);
  cout << s.peek();
  s.pop();
  s.print();
  cout << s.peek();
}
