def func(vote_list):
    candidate_dict = {}
    for name, counter in vote_list:
        counter = int(counter)
        if name not in candidate_dict:
            candidate_dict[name] = 0
        candidate_dict[name] += counter

    return sorted(candidate_dict.items(), key=lambda x: x[0])


def main():
    vote_list = []
    with open("input.txt", "r") as doc:
        for line in doc:
            vote_list.append(line.split())

    for string in func(vote_list):
        print(*string)

def test():
    test_input_1 = [['McCain', '10'], ['McCain', '5'], ['Obama', '9'], ['Obama', '8'], ['McCain', '1']]
    test_input_2 = [['ivanov', '100'], ['ivanov', '500'], ['ivanov', '300'], ['petr', '70'], ['tourist', '1'], ['tourist', '2']]
    test_input_3 = [['bur', '1']]
    assert func(test_input_1) == [('McCain', 16), ('Obama', 17)]
    assert func(test_input_2) == [('ivanov', 900), ('petr', 70), ('tourist', 3)]
    assert func(test_input_3) == [('bur', 1)]

if __name__ == '__main__':
    main()