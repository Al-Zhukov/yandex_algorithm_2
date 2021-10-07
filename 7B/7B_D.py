def solution(n, m, kittens, left, right):
    points = [None] * (2 * n + m)
    for i in range(n):
        points[2 * i] = (left[i], '1_left', i)
        points[2 * i + 1] = (right[i], '3_right', i)
    for i in range(m):
        points[2 * n + i] = (kittens[i], '2_kitten')
    points.sort()

    results = [0] * m
    kitten_counter = 0
    for i in range(2 * n + m):
        if points[i][1] == '1_left':
            results[points[i][2]] -= kitten_counter
        elif points[i][1] == '3_right':
            results[points[i][2]] += kitten_counter
        elif points[i][1] == '2_kitten':
            kitten_counter += 1
    return results

def main():
    n, m = map(int, input().split())
    kittens = list(map(int, input().split()))

    left_borders, right_borders = [None] * m, [None] * m
    for i in range(m):
        left_borders[i], right_borders[i] = map(int, input().split())

    print(*solution(n, m, kittens, left_borders, right_borders))

def test():
    assert solution(2, 2, [1, 2], [0, 1], [2, 3]) == [2, 2]
    assert solution(2, 2, [1, 2], [0, 1], [1, 3]) == [1, 2]
    assert solution(2, 2, [1, 2], [-5, 3], [15, 4]) == [2, 0]
    assert solution(3, 3, [1, 2, 10], [0, 1, 5], [1, 3, 6]) == [1, 2, 0]

if __name__ == '__main__':
    main()