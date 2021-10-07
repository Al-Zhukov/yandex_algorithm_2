def solution(n, left, duration):
    assert len(left) == len(duration)
    assert n == len(left)
    points = [None] * (2 * n)
    for i in range(n):
        points[2 * i] = (left[i], 'start')
        points[2 * i + 1] = (left[i] + duration[i], 'finish')
    points.sort()

    depth_counter = 0
    max_depth = 0
    for i in range(0, 2 * n):
        if points[i][1] == 'finish':
            depth_counter -= 1
        elif points[i][1] == 'start':
            depth_counter += 1
        max_depth = max(depth_counter, max_depth)
    return max_depth

def main():
    n = int(input())
    arrive_time = [None] * n
    inspection_time = [None] * n
    for i in range(n):
        arrive_time[i], inspection_time[i] = map(int, input().split())

    print(solution(n, arrive_time, inspection_time))


def test():
    assert solution(3, [3, 4, 5], [2, 2, 2]) == 2
    assert solution(5, [13, 15, 11, 12, 10], [4, 1, 5, 3, 3]) == 3

if __name__ == '__main__':
    main()