# 버블 정렬
def bubble_sort(arr: list, order_func) -> list:
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # 두 원소의 순서가 order_func와 다르면 교체
            if not order_func(arr[j], arr[j+1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 삽입 정렬
def insertion_sort(arr:list, order_func):
    arr = arr.copy()
    for key_idx in range(1, len(arr)):
        key = arr[key_idx]
        end_idx = key_idx - 1
        for j in range(end_idx, -1, -1):
            # key 원소가 삽입될 곳이 아니면 오른쪽으로 한칸 밀음.
            # 삽입될 곳이면 (order func 에 부합하면) 밀지 않고 break
            if order_func(arr[j], key): break
            arr[j + 1] = arr[j]
            j -= 1
        # 밀고 남은 공간에 key 삽입
        arr[j + 1] = key
    return arr

# 증가, 감소 함수 - sort 함수의 order_func 용
def asc_func(e1, e2): return e1 < e2
def desc_func(e1, e2): return e1 > e2

# Enter 입력을 기다리는 함수
def wait_enter():
    while True:
        if '' == input("Press 'Enter' to return to the menu..."): break


# 소팅 할 전역 배열
array = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'monkey', 'kangaroo', 'penguin', 'koala', 'hippo']

# menu 함수
def menu():
    while True:
        print("숫자를 입력하여 메뉴를 선택하세요. (1) Bubble Sorting. (2) Insertion Sorting. (3) Exit.")
        cmd = ''
        try:
            cmd = int(input())
        except:
            continue

        if cmd == 1:
            print(f"BUBBLE SORT"
                  f"------------------------------------------------------------------------------------\n"
                  f"[Input String]: {array}\n"
                  f"[Ascending order]: {bubble_sort(array, asc_func)}\n"
                  f"[Descending order]: {bubble_sort(array, desc_func)}\n"
                  f"----------------------------------------------------------------------------------------------")
            wait_enter()
        elif cmd == 2:
            print(f"INSERTION SORT"
                  f"------------------------------------------------------------------------------------\n"
                  f"[Input String]: {array}\n"
                  f"[Ascending order]: {insertion_sort(array, asc_func)}\n"
                  f"[Descending order]: {insertion_sort(array, desc_func)}\n"
                  f"----------------------------------------------------------------------------------------------")
            wait_enter()
        elif cmd == 3:
            break


# main
menu()


