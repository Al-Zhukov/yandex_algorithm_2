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

def solution(array, xl, xr):
    answer_l = lbinsearch(0, len(array) - 1, check_l, (array, xl))
    answer_r = rbinsearch(0, len(array) - 1, check_r, (array, xr))
    return answer_r + 1 - answer_l

def main():
    N = int(input())
    a = list(map(int, input().split()))
    assert len(a) == N
    a = sorted(a)

    K = int(input())
    answers = []
    for _ in range(K):
        L, R = map(int, input().split())
        answers.append(solution(a, L, R))
    print(*answers)


def test():
    assert lbinsearch(0, 4, check_l, ([1, 3, 4, 10, 10], 1)) == 0
    assert rbinsearch(0, 4, check_r, ([1, 3, 4, 10, 10], 5)) == 2
    assert solution([1, 3, 4, 10, 10], 1, 10) == 5
    assert solution([1, 3, 4, 10, 10], 2, 9) == 2
    assert solution([1, 3, 4, 10, 10], 3, 4) == 2
    assert solution([1, 3, 4, 10, 10], 2, 2) == 0
    assert solution([1, 1, 1, 1, 1], 1, 1) == 5
    assert solution([1, 1, 1, 1, 1], 2, 2) == 0
    assert solution([1, 1, 1, 1, 1], 0, 0) == 0

if __name__ == '__main__':
    main()