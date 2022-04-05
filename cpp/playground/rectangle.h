#pragma once
class Rectangle {
private:
  int width;
  int height;

public:
  Rectangle();
  Rectangle(int width, int height);
  int area();
  int perimeter();
};
