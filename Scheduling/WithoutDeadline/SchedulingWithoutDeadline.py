def knap_sack(d, m):
    '''
    Scheduling without deadline algorithm
    Runtime: O(n log(n))
    * Initial sort time O(nlog(n))
    * First loop O(n)
    * Sort O(n log(n))
    * Second loop O(n)
    :param d: sorted sacks by weight that hold in them keys (value,weight)
    :param m: max weight we can hold
    :return: the sorted vector of the parameters and another vector with the amount that should be taken from the sack
    '''
    for sack in d:  # Create the list of the items
        sack['v/w'] = sack['v'] / sack['w']
    d.sort(key=lambda x: x['v/w'], reverse=True)

    w = 0
    i = 0
    ret_vec = []
    while i < len(d) and w < m:
        if (d[i]['w'] + w <= m):
            ret_vec.append(1)
            w += d[i]['w']
        else:
            ret_vec.append((m - w) / d[i]['w'])
            w += m - w
        i += 1
    return d, ret_vec


d = [{'w': 10, 'v': 20}, {'w': 20, 'v': 30}, {'w': 30, 'v': 66}, {'w': 40, 'v': 40}, {'w': 50, 'v': 60}]
print(knap_sack(d, 100))
