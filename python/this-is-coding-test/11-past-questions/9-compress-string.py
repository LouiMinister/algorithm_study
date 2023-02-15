# 문자열 압축

def solution(s):
    res = len(s)
    for unit in range(1, len(s)//2 + 1):
        prev = s[0:unit]
        cur_len = unit
        unit_cnt = 1
        # unit 단위로 반복,
        for unit_start_idx in range(unit, len(s), unit):
            unit_end_idx = min(len(s), unit_start_idx + unit)
            cur = s[unit_start_idx:unit_end_idx]
            # 이전 unit이랑 같은 경우
            if cur == prev:
                unit_cnt += 1
            # 이전 unit이랑 다른 경우
            else:
                # 현재 unit을 cur_len에 반영
                cur_len += len(cur)
                # unit 개수가 2개 이상인 경우 cur_len에 반영
                if unit_cnt >= 2: cur_len += len(str(unit_cnt))
                # prev, unit_cnt 초기화
                prev = cur
                unit_cnt = 1
        if unit_cnt >= 2: cur_len += len(str(unit_cnt))
        res = min(res, cur_len)
    return res
print(solution('a'))