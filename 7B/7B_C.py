def solution_with_check(m, left, right):
    # с проверкой покрытия целевого отрезка перед тем, как строить решение
    assert len(left) == len(right)
    n = len(left)
    points = [None] * (2 * (n + 1))
    segments = [None] * n
    for i in range(n):
        segments[i] = (left[i], right[i])
        points[2 * i] = (left[i], '1_start', i, (left[i], right[i]))
        points[2 * i + 1] = (right[i], '2_finish', i, (left[i], right[i]))
    points[2 * n] = (0, '3_segment_left')
    points[2 * n + 1] = (m, '0_segment_right')
    points.sort()
    segments.sort()

    # проверяем есть покрыт ли [0, M] отрезками в принципе
    depth_counter = 0
    check_depth = False
    for i in range(len(points)):
        if points[i][1] == '2_finish':
            depth_counter -= 1
        elif points[i][1] == '1_start':
            depth_counter += 1
        elif points[i][1] == '3_segment_left':
            check_depth = True
        elif points[i][1] == '0_segment_right':
            check_depth = False
        if check_depth == True:
            if depth_counter == 0:
                return 'No solution'

    # ищем оптимальное покрытие, если оно существует
    border = 0
    segment_counter = 0
    segments_to_answer = []

    while border < m and segment_counter < n:
        best_segment = segments[segment_counter]
        max_border = best_segment[1]
        while segment_counter < n and segments[segment_counter][0] <= border:
            if segments[segment_counter][1] > max_border:
                best_segment = segments[segment_counter]
                max_border = best_segment[1]
            segment_counter += 1
        segments_to_answer.append(best_segment)
        border = max_border

    return segments_to_answer

def solution(m, left, right):
    # строим решение и в процессе проверяем покрытие целевого отрезка
    assert len(left) == len(right)
    n = len(left)

    segments = [None] * n
    for i in range(n):
        segments[i] = (left[i], right[i])
    segments.sort()

    # ищем оптимальное покрытие
    border = 0
    segment_counter = 0
    segments_to_answer = []

    while border < m and segment_counter < n:
        best_segment = segments[segment_counter]
        max_border = best_segment[1]

        while segment_counter < n and segments[segment_counter][0] <= border:
            if segments[segment_counter][1] > max_border:
                best_segment = segments[segment_counter]
                max_border = best_segment[1]
            segment_counter += 1

        if len(segments_to_answer) > 0:
            if segments_to_answer[-1][1] < best_segment[0]:
                return 'No solution'
        elif len(segments_to_answer) == 0:
            if best_segment[0] > 0:
                return 'No solution'

        segments_to_answer.append(best_segment)
        border = max_border

    if segments_to_answer[-1][1] < m:
        return 'No solution'
    return segments_to_answer

def main():
    m = int(input())
    left_borders = []
    right_borders = []

    left, right = map(int, input().split())
    while (left, right) != (0, 0):
        left_borders.append(left)
        right_borders.append(right)
        left, right = map(int, input().split())

    answer = solution(m, left_borders, right_borders)
    if answer != 'No solution':
        print(len(answer))
        for line in answer:
            print(*line)
    else:
        print(answer)


def test():
    def generate_input():
        import random
        m = random.randint(2, 10)
        n = random.randint(5, 10)
        left_borders = [None] * n
        right_borders = [None] * n
        for i in range(n):
            left_borders[i] = random.randint(-10, 10)
            right_borders[i] = left_borders[i] + random.randint(0, 10)
        return (m, left_borders, right_borders)
    
    for sol in [solution, solution_with_check]:
        assert sol(1, [-1, -5, 2], [0, -3, 5]) == 'No solution'
        assert sol(1, [-1, 0], [0, 1]) == [(0,1)]
        assert sol(500, [-1000, 5000, 15, 13, 18, 15, -5000, -8000], [13, 50000, 499, 18, 500, 18, 5, -3]) == [(-1000, 13), (13, 18), (18, 500)]
        assert sol(5, [-4, -9, -5, -3, -4, -5, -4], [-4, -9, 0, 4, 0, 1, -1]) == 'No solution'
        assert sol(1234, [1], [1234]) == 'No solution'

if __name__ == '__main__':
    main()