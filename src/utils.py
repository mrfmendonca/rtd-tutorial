def concat_lists(l1, l2):
    l3 = l1 + l2
    return l3

def sum_lists(l1, l2):
    assert type(l1) == list and type(l2) == list, "ERROR: l1 and l2 must be lists."
    assert len(l1) == len(l2), "ERROR: l1 and l2 must have the same size"
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i] + l2[i])
    return l3

def mult_list(l1, l2):
    assert len(l1) == len(l2), "ERROR: l1 and l2 must have the same size"
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i] * l2[i])
    return l3