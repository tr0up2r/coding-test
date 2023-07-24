def solution(id_list, report, k):
    reported_dict, user_dict = dict(), dict()

    for id in id_list:
        reported_dict[id] = set()
        user_dict[id] = 0

    for r in report:
        user, reported_user = r.split()
        reported_dict[reported_user].add(user)

    for id in id_list:
        if len(reported_dict[id]) >= k:
            for u in reported_dict[id]:
                user_dict[u] += 1

    return list(user_dict.values())
