# 산타의 선물 공장 2
import math
from collections import deque


def mis(): return map(int, input().split(' '))


# 초기화
# 한개의 Operation에 O(N) 이 걸리면 망함.
# 물건 나누기는 ㄱㅊ - 100개밖에 안나옴

# 선물
# 노드간의 연결 끊고 이동하기 - 벨트의 크기
# 앞에 있는 선물, 뒤에 있는 선물
# idx로 특정 선물의 앞 뒤에 바로 접근할 수 있어야 함.
class Gift:
    head = None
    tail = None
    num = 0

    def __init__(self, num):
        self.num = num


# 벨트
# 벨트의 크기, 맨앞, 맨뒤
class Belt:
    first = None
    last = None
    size = 0

    def clear(self):
        self.first = None
        self.last = None
        self.size = 0

    # 앞에다 붙히는 경우만
    def add_gifts(self, first_gift, last_gift, gift_cnt):
        if first_gift is None: return

        # 새로 들어온 기프트 처리
        if first_gift.head: first_gift.head.tail = None
        if last_gift.tail: last_gift.tail.head = None
        first_gift.head = None
        last_gift.tail = self.first
        # 원래 있던 기프트 처리
        if self.first: self.first.head = last_gift
        # 컨테이너 포인터 처리
        self.first = first_gift
        if self.size == 0:
            self.last = last_gift
        # 컨테이너 선물 개수 처리
        self.size += gift_cnt

    def add(self, gift):
        self.add_gifts(gift, gift, 1)

    def add_back(self, gift):
        if self.size == 0:
            self.first = gift
            self.last = gift
            self.size += 1
        else:
            # 들어 온거 잇기
            gift.head = self.last
            # 원래 있던거 있기
            self.last.tail = gift
            # 포인터 변경
            self.last = gift
            self.size += 1
    def pop_first(self):
        res = None
        if self.size == 1:
            self.clear()
            res = self.first
        elif self.size > 1:
            res = self.first
            self.first = self.first.tail
            self.first.head.tail = None
            self.first.head = None
            self.size -= 1
        return res


cmd_cnt = int(input())  # 1 ~ 100,000
temp_input = list(mis())
belt_cnt, gift_cnt = temp_input[1], temp_input[2]  # 1 ~ 100,000 / 1~ 100,000
belts = [None] + [Belt() for _ in range(belt_cnt)]
gifts = [None]

for gift_idx, belt_idx in enumerate(temp_input[3:]):
    gift_idx += 1
    cur_gift = Gift(gift_idx)
    cur_belt = belts[belt_idx]
    gifts.append(cur_gift)
    cur_belt.add_back(cur_gift)

# for gift in gifts[1:]:
#     print(gift.head.num if gift.head else None, gift.num, gift.tail.num if gift.tail else None)
# print('---')
# for belt in belts[1:]:
#     print(belt.first.num if belt.first else None, belt.size, belt.last.num if belt.last else None)


# 함수

# src -> dst 벨트 옮김. 앞쪽으로 옮겨짐
# 옮긴 뒤에 dst 벨트 선물 개수 출력
def move(src, dst):
    global belts
    src_belt = belts[src]
    dst_belt = belts[dst]
    dst_belt.add_gifts(src_belt.first, src_belt.last, src_belt.size)
    src_belt.clear()
    print(dst_belt.size)


# 교환 - 앞 물건만 교체
# 하나가 없다면 dst 번째 벨트 선물 개수 출력
def change(src, dst):
    global belts
    to_src = belts[dst].pop_first()
    to_dst = belts[src].pop_first()

    if to_src: belts[src].add(to_src)
    if to_dst: belts[dst].add(to_dst)
    print(belts[dst].size)


# 나누기 - 앞에서 n/2 개 까지 선물을 src -> dst 앞으로 옮김
# 옮기고 개수 출력
def divide(src, dst):
    global belts
    moving_gift_cnt = math.floor(belts[src].size / 2)
    if moving_gift_cnt == 0:
        print(belts[dst].size)
        return


# 선물정보얻기
# 선물 번호 p -> 앞번호(없으면 -1) + 2 * 뒷번호(없으면 -1) 출력
def get_gift(gift_idx):
    global gifts
    gift = gifts[gift_idx]
    gift_head = gift.head.num if gift.head else -1
    gift_tail = gift.tail.num if gift.tail else -1
    # print('@@@@', gift_head, gift_tail)
    print(gift_head + 2 * gift_tail)


# 벨트정보얻기
# 맨앞(-1) + 맨뒤(-1) * 2 + 선물개수*3
def get_belt(belt_idx):
    global belts
    gift_first = belts[belt_idx].first.num if belts[belt_idx].first else -1
    gift_last = belts[belt_idx].last.num if belts[belt_idx].last else -1
    print(gift_first + 2 * gift_last + belts[belt_idx].size * 3)

# 실행
for _ in range(cmd_cnt-1):
    temp_input = list(mis())
    cmd_code = temp_input[0]
    if cmd_code == 200:
        src, dst = temp_input[1], temp_input[2]
        move(src, dst)
    elif cmd_code == 300:
        src, dst = temp_input[1], temp_input[2]
        change(src, dst)
    elif cmd_code == 400:
        src, dst = temp_input[1], temp_input[2]
        divide(src, dst)
    elif cmd_code == 500:
        gift_num = temp_input[1]
        get_gift(gift_num)
    elif cmd_code == 600:
        belt_num = temp_input[1]
        get_belt(belt_num)

    # print('---------------', temp_input)
    # for gift in gifts[1:]:
    #     print(gift.head.num if gift.head else None, gift.num, gift.tail.num if gift.tail else None)
    # print('-----')
    # for belt in belts[1:]:
    #     print(belt.first.num if belt.first else None, belt.size, belt.last.num if belt.last else None)


# idx -1 해줘야함
# 명령에 따라 switch



# 1 5
# 2 3 4
#
# 6