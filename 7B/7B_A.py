def solution(n, left, right):
    assert len(left) == len(right)
    assert n == len(left)
    points = [None] * (2 * n)
    for i in range(n):
        points[2 * i] = (left[i], 'left')
        points[2 * i + 1] = (right[i], 'right')
    points.sort()

    depth_counter = 0
    sum_lenght = 0
    for i in range(0, 2 * n):
        if points[i][1] == 'right':
            sum_lenght += points[i][0] - points[i - 1][0]
            depth_counter -= 1
        elif points[i][1] == 'left':
            if depth_counter > 0:
                sum_lenght += points[i][0] - points[i - 1][0]
            depth_counter += 1
    return sum_lenght

def main():
    n = int(input())
    left_borders = [None] * n
    right_borders = [None] * n
    for i in range(n):
        left_borders[i], right_borders[i] = map(int, input().split())
    print(solution(n, left_borders, right_borders))


def test():
    assert solution(1, [10], [20]) == 10
    assert solution(1, [10], [10]) == 0
    assert solution(2, [10, 20], [20, 40]) == 30

if __name__ == '__main__':
    main()