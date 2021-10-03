def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def check(lenght, params):
    number, array = params

    segment_counter = 1
    segment_end = array[0] + lenght
    for position in range(len(array)):
        if array[position] > segment_end:
            segment_counter += 1
            segment_end = array[position] + lenght
    return segment_counter <= number

def solution(k, array):
    array = sorted(array)
    return lbinsearch(0, array[-1] - array[0], check, (k, array))

def solution_recursive(k, n, array):
    if n == 1:
        return 1
    elif n <= 0:
        return 0

    i = 1
    while (i < n) and (array[i] - array[0] <= k):
        i += 1
    return 1 + solution_recursive(k, n - i - 1, array[(i+1):])

def main():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    assert len(array) == n
    print(solution(k, array))

def test():
    assert solution_recursive(2, 6, [1, 2, 3, 7, 8, 9]) == 2
    assert solution(2, [1, 2, 3, 9, 8, 7]) == 2

if __name__ == '__main__':
    main()