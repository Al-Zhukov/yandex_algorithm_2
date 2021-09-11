def main():
    with open("input.txt", "r") as doc:
        n = int(doc.readline())
        possible_answers = set(range(1, n+1))
        temp = set()

        for line in doc:
            if 'YES' in line:
                possible_answers &= temp
            elif 'NO' in line:
                possible_answers -= temp
            elif 'HELP' in line:
                break
            else:
                temp = set(map(int, line.split()))
    print(' '.join(map(str, sorted(possible_answers))))

if __name__ == '__main__':
    main()