def func(a):
    have_seen_set = set()
    answers = []
    for i in range(len(a)):
        if a[i] in have_seen_set:
            answers.append('YES')
        else:
            answers.append('NO')
            have_seen_set.add(a[i])
    return '\n'.join(answers)

def main():

    a = list(map(int, input().split()))
    print(func(a))

def test():
    assert func([1, 2, 3, 2, 3, 4]) == 'NO\nNO\nNO\nYES\nYES\nNO'

if __name__ == '__main__':
    main()