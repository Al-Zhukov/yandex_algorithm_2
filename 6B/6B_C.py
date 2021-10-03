def lbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l

def calc_cubic(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x ** 1 + d

def check(x, params):
    a, b, c, d = params
    return calc_cubic(a, b, c, d, x) > 0

def solution(a, b, c, d, eps):
    if a < 0:
        a, b, c, d = -a, -b, -c, -d
    left_border = -1000
    right_border = 1000
    while calc_cubic(a, b, c, d, left_border) > 0:
        left_border *= 10
    while calc_cubic(a, b, c, d, right_border) < 0:
        right_border *= 10

    return lbinsearch(left_border, right_border, eps, check, (a, b, c, d))

def main():
    a, b, c, d = map(int, input().split())
    eps = 10 ** (-6)
    print(solution(a, b, c, d, eps))

def test():
    eps = 10 ** (-6)
    assert abs(solution(1, -3, 3, -1, eps) - 1) < eps
    assert abs(solution(-1, -6, -12, -7, eps) - (-1)) < eps

if __name__ == '__main__':
    main()