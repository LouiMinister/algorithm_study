# 섬 연결하기

def find_group_idx(groups, n):
    for idx, group in enumerate(groups):
        for e in group:
            if e == n:
                return idx
    return -1


def solution(n, costs):
    result = 0
    costs = sorted(costs, key=lambda x: x[2])
    groups = []
    # print(costs)

    # 순회하면서
    for node1, node2, cost in costs:
        # 그룹이 통일되면 탈출

        node1_group_idx = find_group_idx(groups, node1)
        node2_group_idx = find_group_idx(groups, node2)

        # 두 노드가 그룹에 존재하지 않으면
        if node1_group_idx == -1 and node2_group_idx == -1:
            # 두 노드를 한 그룹에 추가
            groups.append([node1, node2])
            result += cost
        # 두 노드가 그룹에 존재하면
        elif node1_group_idx >= 0 and node2_group_idx >= 0:
            if node1_group_idx != node2_group_idx:
                # 그룹 병합
                groups[node1_group_idx] += groups[node2_group_idx]
                groups.pop(node2_group_idx)
                result += cost
        # 한 노드만 그룹에 존재하면
        else:
            # print('hi')
            will_group, will_node = None, None
            if node1_group_idx >= 0:
                will_group = node1_group_idx
                will_node = node2
            else:
                will_group = node2_group_idx
                will_node = node1
            # print(node1_group_idx, node2_group_idx, will_group, will_node)
            groups[will_group].append(will_node)
            result += cost
        # print(groups)
    # print(groups)
    return result