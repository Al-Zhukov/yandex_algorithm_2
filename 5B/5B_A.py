def make_prefix_sum(n, array):
    prefixsum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsum[i] = prefixsum[i - 1] + array[i - 1]
    return prefixsum

def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l - 1]

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    prefix_sum = make_prefix_sum(n, a)



def test():
    assert make_prefix_sum(4, [1, 2, 3, 4]) == [0, 1, 3, 6, 10]
    assert rsq([0, 1, 3, 6, 10], 1, 1) == 1
    assert rsq([0, 1, 3, 6, 10], 4, 4) == 4
    assert rsq([0, 1, 3, 6, 10], 1, 4) == 10


if __name__ == '__main__':
    main()