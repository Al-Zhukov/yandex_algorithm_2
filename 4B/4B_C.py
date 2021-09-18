def func(text_list):
    word_dict = {}
    for word in text_list:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

    return sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))


def main():
    text_list = []
    with open("input.txt", "r") as doc:
        for line in doc:
            text_list += line.split()

    for string in func(text_list):
        print(string[0])

def test():
    test_input_1 = ['hi', 'hi', 'what', 'is', 'your', 'name', 'my', 'name', 'is', 'bond', 'james', 'bond', 'my', 'name',
                    'is', 'damme', 'van', 'damme', 'claude', 'van', 'damme', 'jean', 'claude', 'van', 'damme']
    test_output_1 = [('damme', 4), ('is', 3), ('name', 3), ('van', 3), ('bond', 2), ('claude', 2), ('hi', 2), ('my', 2),
                     ('james', 1), ('jean', 1), ('what', 1), ('your', 1)]
    test_input_2 = ['ai', 'ai', 'ai', 'ai', 'ai', 'ai', 'ai', 'ai', 'ai', 'ai']
    test_output_2 = [('ai', 10)]
    test_input_3 = ['oh', 'you', 'touch', 'my', 'tralala', 'mmm', 'my', 'ding', 'ding', 'dong']
    test_output_3 = [('ding', 2), ('my', 2), ('dong', 1), ('mmm', 1), ('oh', 1), ('touch', 1), ('tralala', 1), ('you', 1)]
    assert func(test_input_1) == test_output_1
    assert func(test_input_2) == test_output_2
    assert func(test_input_3) == test_output_3

if __name__ == '__main__':
    main()