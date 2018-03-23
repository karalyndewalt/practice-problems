
# in: [(1,3), (2,4), (5,6)]
# out: [(1,4), (5,6)]


def merge_intervals(in_list):

    if not in_list:
        return []

    lst = sorted(in_list)
    out = [lst[0]]

    for i in range(1, len(lst)):
        last_out = out[-1]
        current = lst[i]
        if last_out[1] >= current[0]:
            out[-1] = (last_out[0], max(current[1], last_out[1]))
        else:
            out.append(current)

    return out
