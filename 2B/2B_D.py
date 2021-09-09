
def func(L, K, legs):
    center = L / 2
    left_leg, right_leg = None, None
    for i in range(K):
        if legs[i] < center:
            left_leg = legs[i]
        elif legs[i] >= center and (right_leg is None):
            right_leg = legs[i]
            break
    if left_leg + 1 > center:
        return [left_leg]
    else:
        return [left_leg, right_leg]

def main():
    L, K = map(int, input().split())
    legs = list(map(int, input().split()))
    print(*func(L, K, legs))

def test():
    assert func(5, 2, [0, 2]) == [2]
    assert func(13, 4, [1, 4, 8, 11]) == [4, 8]
    assert func(14, 6, [1, 6, 8, 11, 12, 13]) == [6, 8]
    assert func(15, 6, [1, 2, 3, 4, 6, 7]) == [7]
    assert func(1, 7, [0, 1, 2, 3, 4, 6, 7]) == [0]
    assert func(2, 9, [0, 1, 10, 23, 24, 32, 40, 72, 79]) == [0, 1]

if __name__ == '__main__':
    main()