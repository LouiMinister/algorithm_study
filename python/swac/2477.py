import heapq
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    rc_spots_cnt, rp_spots_cnt, cs_cnt, cs_rc_num, cs_rp_num = map(int, input().split(' '))
    rc_spots_time = [0] + list(map(int, input().split(' ')))
    rp_spots_time = [0] + list(map(int, input().split(' ')))
    cs_vis_time_list = [0] + list(map(int, input().split(' ')))
    cs_vis_time_dict = dict()
    for cur_cs in range(1, cs_cnt + 1):
        cur_cs_vis_time = cs_vis_time_list[cur_cs]
        if cur_cs_vis_time not in cs_vis_time_dict:
            cs_vis_time_dict[cur_cs_vis_time] = []
        cs_vis_time_dict[cur_cs_vis_time].append(cur_cs)

    cs = [(0,0) for _ in range(cs_cnt + 1)] # 고객별 이용한 rc, rp
    rc_spots = [0] + [None] * rc_spots_cnt
    rp_spots = [0] + [None] * rc_spots_cnt
    rc_queue = []
    rp_queue = deque()

    finished_cs_cnt = 0
    res = 0

    for cur_time in range(200000):

        # 시간 경과 로직
        # rc work
        rc_finished = [] # (rc_idx, cs)
        for rc_i in range(1, rc_spots_cnt+1):
            cur_rc = rc_spots[rc_i]
            if cur_rc is not None:
                cur_rc[1] += 1
                if cur_rc[1] == rc_spots_time[rc_i]:
                    heapq.heappush(rc_finished, (rc_i, cur_rc[0]))
                    rc_spots[rc_i] = None

        while rc_finished:
            rc_num, cs_num = heapq.heappop(rc_finished)
            rp_queue.append((cs_num, rc_num))

        # rp work
        rp_finished = []
        for rp_i in range(1, rp_spots_cnt+1):
            cur_rp = rp_spots[rp_i]
            if cur_rp is not None:
                cur_rp[1] += 1
                if cur_rp[1] == rp_spots_time[rp_i]:
                    rp_finished.append((cur_rp[0], rp_i))
                    rp_spots[rp_i] = None
                # 전부 끝낸사람은 pop & insert

        while rp_finished:
            ((cs_num, rc_num), rp_num) = rp_finished.pop()
            finished_cs_cnt += 1
            if rc_num == cs_rc_num and rp_num == cs_rp_num:
                res += cs_num

        if finished_cs_cnt >= cs_cnt:
            if res > 0:
                print(f'#{test_case} {res}')
            else:
                print(f'#{test_case} -1')
            break


        # 도착하는 시간이 현재이면 rc 대기 큐에 손님 넣기
        if cur_time in cs_vis_time_dict:
            for cs in cs_vis_time_dict[cur_time]:
                heapq.heappush(rc_queue, cs)

        # rc 대기 큐 오름차순 정렬
        # rc 낮은곳부터 비어있는 곳 있으면 손님 넣기
        for rc_i in range(1, rc_spots_cnt + 1):
            if len(rc_queue) == 0: break
            if rc_spots[rc_i] is None:
                popped_cs = heapq.heappop(rc_queue)
                rc_spots[rc_i] = [popped_cs, 0]

        # rp 대기 큐 (먼저 들어간 사람이 먼저 나옴)
        # rp 낮은곳부터 비어있는 곳 있으면 손님 넣기
        for rp_i in range(1, rp_spots_cnt + 1):
            if len(rp_queue) == 0: break
            if rp_spots[rp_i] is None:
                popped_cs, popped_rc_num = rp_queue.popleft()
                rp_spots[rp_i] = [(popped_cs, popped_rc_num), 0]



        # 동시에 rc에서 일 끝난 경우 접수번호 작은 고객이 먼저 들어감

    # 출력
    # 해당 고객 합 출력 or 없으면 -1 출력