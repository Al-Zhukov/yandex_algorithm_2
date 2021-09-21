def make_prefix_sum(n, array):
    prefixsum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsum[i] = prefixsum[i - 1] + array[i - 1]
    return prefixsum

def max_rsq(prefixsum):
    if len(prefixsum) == 2:
        return prefixsum[1]

    left = prefixsum[0]
    max_sum = prefixsum[1] - left
    for i in range(1, len(prefixsum)):
        if prefixsum[i] < left:
            left = prefixsum[i]
        else:
            sum = prefixsum[i] - left
            if sum > max_sum:
                max_sum = sum
    return max_sum


def main():
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = make_prefix_sum(n, a)
    print(max_rsq(prefix_sum))

def test():
    assert make_prefix_sum(4, [1, 2, 3, 4]) == [0, 1, 3, 6, 10]
    assert make_prefix_sum(4, [4, -10, 5, 4]) == [0, 4, -6, -1, 3]
    assert make_prefix_sum(4, [-1, -2, -3, -4]) == [0, -1, -3, -6, -10]
    assert make_prefix_sum(4, [-1, 3, -3, -4]) == [0, -1, 2, -1, -5]
    assert max_rsq([0, 1, 3, 6, 10]) == 10
    assert max_rsq([0, 4, -6, -1, 3]) == 9
    assert max_rsq([0, -1, -3, -6, -10]) == -1
    assert max_rsq([0, -1, 2, -1, -5]) == 3

if __name__ == '__main__':
    main()