a = [1, 3, 4, 6, 7, 8, 9, 11, 15, 17, 19, 21, 22, 25, 29, 33, 38, 69, 107]


def binary_search(start, end, n, d_list):
    """
    每次把列表规模折半，查找一个数据最多只需要2的n次方 < len(d_list),是2的多少次方，就是最多查多少次。
    假如列表长度为200，那最多只需查询8次(2**8次方）
    """
    if start < end:  # 查找的范围[start:end]依然大于0个
        mid = (start + end) // 2  # 找到中间位置
        if d_list[mid] > n:  # 如果中间的这个值比要找的n大，代表要往d_list[mid]左边找
            print("go left", start, mid, end, "--", d_list[start], d_list[mid], d_list[end - 1])
            binary_search(start, mid, n, d_list)
        elif d_list[mid] < n:  # 要往右边找，继续折半
            print("go right..", start, mid, end, "--", d_list[start], d_list[mid], d_list[end - 1])
            binary_search(mid + 1, end, n, d_list)
        else:  # 找到了
            print("find:", d_list[mid], mid)
    else:  # 假设start=9,end=9, 那d_list[9:9]已经取不到值了，在这种情况下，只能说明，要找的这个值不在这个列表里
        print("cannot find %s in this data list" % n)


binary_search(0, len(a), 1, a)
