def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def check(x, params):
    A, K, B, M, X = params
    return (A * (x - x // K) + B * (x - x // M)) >= X

def solution(A, K, B, M, X):
    return lbinsearch(1, X, check, (A, K, B, M, X))

def main():
    A, K, B, M, X = map(int, input().split())
    print(solution(A, K, B, M, X))

def test():
    assert solution(1, 2, 1, 3, 10) == 8
    assert solution(1, 2, 1, 3, 11) == 9
    assert solution(19, 3, 14, 6, 113) == 4

if __name__ == '__main__':
    main()