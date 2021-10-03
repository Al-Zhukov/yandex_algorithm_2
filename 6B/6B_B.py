def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    if check(l, checkparams):
        return l
    else:
        return l + 1

def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    if check(l, checkparams):
        return l
    else:
        return l - 1

def check_l(m, params):
    array, x = params
    return array[m] >= x

def check_r(m, params):
    array, x = params
    return array[m] <= x

def solution(array, x):
    answer_l = lbinsearch(0, len(array) - 1, check_l, (array, x))
    answer_r = rbinsearch(0, len(array) - 1, check_r, (array, x))
    if answer_l > len(array) - 1 or answer_r < 0:
        return (0, 0)
    elif array[answer_l] == x and array[answer_r] == x:
        return (answer_l + 1, answer_r + 1)
    else:
        return (0, 0)

def main():
    N = int(input())
    a = list(map(int, input().split()))
    assert len(a) == N

    K = int(input())
    for number in map(int, input().split()):
        print(*solution(a, number))

def test():
    assert solution([1, 2, 2, 3], 4) == (0, 0)
    assert solution([1, 2, 2, 3], 3) == (4, 4)
    assert solution([1, 2, 2, 3], 2) == (2, 3)
    assert solution([1, 2, 2, 3], 1) == (1, 1)
    assert solution([1, 2, 2, 3], 0) == (0, 0)
    assert solution([1, 3, 3, 3, 3, 6, 8, 8, 9, 10], 2) == (0, 0)

if __name__ == '__main__':
    main()