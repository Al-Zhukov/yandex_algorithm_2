def naive(S, A, B, C):
    # Наивное решение за O(N^3)
    for i in range(A[0]):
        for j in range(B[0]):
            for k in range(C[0]):
                if A[i + 1] + B[j + 1] + C[k + 1] == S:
                    return [i, j, k]
    return [-1]

def func_with_dict(S, A, B, C):
    # Решение через перебор А и В и проверку С в хэш-таблице. O(N^2)
    C_dict = {}
    for i in range(C[0]):
        if C[i + 1] not in C_dict:
            C_dict[C[i + 1]] = i

    for i in range(A[0]):
        for j in range(B[0]):
            if S - A[i + 1] - B[j + 1] in C_dict:
                return [i, j, C_dict[S - A[i + 1] - B[j + 1]]]
    return [-1]

def func_with_two_index(S, A, B, C):
    # Решение через перебор А и два встречных указателя, бегущих по В и С. O(N^2)
    B_order = []
    for i in range(B[0]):
        B_order.append([B[i + 1], i])

    C_order = []
    C_dict = {}
    for i in range(C[0]):
        if C[i + 1] not in C_dict:
            C_dict[C[i + 1]] = i
            C_order.append([C[i + 1], i])

    B_order = sorted(B_order, key=lambda x: x[0])
    C_order = sorted(C_order, key=lambda x: x[0])

    answers = []
    for i in range(A[0]):
        left = 0
        right = len(C_order) - 1
        while (left < B[0]) and (right >= 0):
            if (B_order[left][0] + C_order[right][0] +  A[i + 1]) == S:
                answers.append([i, B_order[left][1], C_order[right][1]])
                left += 1
            elif B_order[left][0] + C_order[right][0] > S - A[i + 1]:
                right -= 1
            else:
                left += 1

    if len(answers) == 0:
        return [-1]
    else:
        return sorted(answers)[0]

def main():
    S = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    print(*func_with_dict(S, A, B, C))

def test():
    import random
    func_to_check = func_with_dict
    repeats = 10

    assert func_to_check(3, [2, 1, 2], [2, 3, 1], [2, 3, 1]) == [0, 1, 1]
    assert func_to_check(10, [1, 5], [1, 4], [1, 3]) == [-1]
    assert func_to_check(5, [4, 1, 2, 3, 4], [3, 5, 2, 1], [4, 5, 3, 2, 2]) == [0, 1, 2]

    for _ in range(repeats):
        S = random.randint(3, 15)
        a = random.randint(1, 5)
        A = [a] + [random.randint(1, 5) for _ in range(a)]
        b = random.randint(1, 5)
        B = [b] + [random.randint(1, 5) for _ in range(b)]
        c = random.randint(1, 5)
        C = [c] + [random.randint(1, 5) for _ in range(c)]

        if func_to_check(S, A, B, C) != naive(S, A, B, C):
            print('Houston, we have a problem!')
            print(S, A, B, C)
            print('naive output', naive(S, A, B, C))
            print('func output', func_to_check(S, A, B, C))
            print('-----------')

if __name__ == '__main__':
    main()