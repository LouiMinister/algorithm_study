#include <iostream>

using namespace std;

template <typename T> class CQueue { // 원형큐
private:
  T *queue;
  int front;
  int rear;
  int capacity;

  bool isFull() {
    return front == (rear + 1) % capacity;
  } // 일부로 한칸을 항상 비우도록 해서 capacity - 1 개수만큼 차면 full

  void doubleCapacity() {
    T *newQueue = new T[capacity * 2];
    int ni = 0;
    int i = front;
    while (true) {
      i = (i + 1) % capacity;
      newQueue[ni++] = queue[i];
      if (i == rear)
        break;
    }
    delete queue;
    queue = newQueue;
    front = capacity * 2 - 1;
    rear = capacity - 2;
    capacity = capacity * 2;
  }

public:
  CQueue(int v) : capacity(v) {
    if (capacity < 1)
      throw "Queue capacity must be > 0";
    queue = new T[capacity];
    front = rear = 0;
  }

  void enqueue(T v) {
    if (isFull()) {
      doubleCapacity();
    }
    rear = (rear + 1) % capacity;
    queue[rear] = v;
  }

  void dequeue() {
    if (isEmpty()) {
      cout << "queue is emtpy" << endl;
      return;
    }
    front = (front + 1) % capacity;
    queue[front] = 0;
  }

  bool isEmpty() { return front == rear; }

  void print() {
    for (int i = 0; i < capacity; i++) {
      cout << queue[i] << ' ';
    }
    cout << '\n';
  }
};

int main() {
  CQueue<int> q(3);
  q.print();
  q.enqueue(1);
  q.enqueue(2);
  q.enqueue(3);
  q.print();
  q.enqueue(4);
  q.enqueue(5);
  q.dequeue();
  q.print();
  q.enqueue(6);
  q.print();
  q.dequeue();
  q.enqueue(7);
  q.print();
  q.enqueue(8);
  q.print();
  q.enqueue(9);
  q.enqueue(10);
  q.enqueue(11);
  q.enqueue(12);
  q.enqueue(13);
  q.enqueue(14);
  q.print();
}
