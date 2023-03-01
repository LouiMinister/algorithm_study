# 보석 쇼핑
def solution(gems):
    result = [0, 999999999999]
    N = len(gems)
    bag = dict()
    bag[gems[0]] = 1
    max_gems = len(set(gems))
    s_i, e_i = 0, 0

    # 계속 반복
    while e_i < N:
        # 가방에 모든 종류의 보석이 있다면 결과 업데이트하기 + s_i 늘리면서 보석 빼기
        # print(bag, s_i, e_i)
        if len(bag) == max_gems:
            # 결과에 업데이트
            if (e_i) - s_i < result[1] - result[0]:
                result = [s_i, e_i]
            gem_will_pop = gems[s_i]
            bag[gem_will_pop] -= 1
            if bag[gem_will_pop] == 0: bag.pop(gem_will_pop)
            s_i += 1
        # 가방에 모든 종류의 보석이 없다면
        else:
            e_i += 1
            if e_i >= N: break
            # 가방에 미리 없다면 e_i 늘리면서 가방에 보석넣기
            gem_will_push = gems[e_i]
            if not (gem_will_push in bag):
                bag[gem_will_push] = 0
            bag[gem_will_push] += 1


    return [result[0 ] +1, result[1 ] +1]
