def dist(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def func(d, X):
    x, y = X[0], X[1]
    if (x >= 0) and (y >= 0) and (x + y <= d):
        return 0
    else:
        min_index, min_value = min(enumerate([dist([0, 0], X), dist([d, 0], X), dist([0, d], X)]), key=lambda x: x[1])
        return min_index + 1

def main():
    d = int(input())
    X = list(map(int, input().split()))
    print(func(d, X))

def test():
    assert func(5, [1, 1]) == 0
    assert func(3, [-1, -1]) == 1
    assert func(4, [4, 4]) == 2
    assert func(4, [2, 2]) == 0

if __name__ == '__main__':
    main()