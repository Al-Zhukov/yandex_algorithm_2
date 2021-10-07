def solution(n, rectangles):
    pi = 3.1415926
    angles = [None] * 2 * n
    r1_max = rectangles[0][0]
    r2_min = rectangles[0][1]
    start_shift = 0
    for i in range(n):
        r1, r2, fi1, fi2 = rectangles[i]
        r1_max = max(r1_max, r1)
        r2_min = min(r2_min, r2)
        angles[2 * i] = (fi1, 'start')
        angles[2 * i + 1] = (fi2, 'finish')
        if fi2 < fi1:
            start_shift += 1
    angles.append((0, 'global_start'))
    angles.sort()
    angles.append((2 * pi, 'finish'))

    result_sum = 0
    depth_counter = start_shift
    for i in range(len(angles)):
        if angles[i][1] == 'start':
            depth_counter += 1
        elif angles[i][1] == 'finish':
            if depth_counter == n:
                result_sum += (r2_min ** 2 - r1_max ** 2) * (angles[i][0] - angles[i - 1][0]) / 2
            depth_counter -= 1

    return result_sum

def main():
    n = int(input())
    rectangles = [None] * n
    for i in range(n):
        rectangles[i] = list(map(float, input().split()))

    print(solution(n, rectangles))


def test():
    assert (solution(2, [[1.0, 2.0, 0.0, 3.0], [1.0, 2.0, 2.0, 1.0]]) - 3.75) < 10 ** (-6)
    assert (solution(2, [[1.0, 2.0, 0.0, 3.0], [1.0, 2.0, 2.0, 1.0]]) - 3.0) < 10 ** (-6)
    assert (solution(2, [[84.68891, 87.08898, 0.76315, 0.42392], [40.00562, 88.88346, 2.39411, 0.42392]]) - 889.0785887) < 10 ** (-6)

if __name__ == '__main__':
    main()