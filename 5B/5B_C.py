def main():
    N, M = map(int, input().split())
    X = [[value, pos + 1] for pos, value in enumerate(map(int, input().split()))]
    Y = [[value, pos + 1] for pos, value in enumerate(map(int, input().split()))]
    assert len(X) == N
    assert len(Y) == M
    X = sorted(X, key=lambda x: x[0])
    Y = sorted(Y, key=lambda x: x[0])

    answers_counter = 0
    answers = [0] * N
    X_pos = 0
    Y_pos = 0
    while X_pos < N and Y_pos < M:
        if X[X_pos][0] + 1 <= Y[Y_pos][0]:
            answers_counter += 1
            answers[X[X_pos][1] - 1] = Y[Y_pos][1]
            X_pos += 1
            Y_pos += 1
        else:
            Y_pos += 1
    print(answers_counter)
    print(*answers)


def test():
    pass

if __name__ == '__main__':
    main()