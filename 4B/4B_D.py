def func(party_list, num_places=450):
    sum = 0
    for party in party_list:
        sum += party[1]

    for i in range(len(party_list)):
        result = party_list[i][1]
        quantity = num_places * result / sum
        int_part = int(quantity // 1)
        party_list[i] += [int_part, quantity - int_part]
    party_list = sorted(party_list, key=lambda x: (x[3], x[2]), reverse=True)

    residuals = num_places
    for party in party_list:
        residuals -= party[2]

    for i in range(residuals):
        party_list[i][2] += 1

    party_dict = {}
    for party_name in party_list:
        party, result = party_name[0], party_name[2]
        party_dict[party] = result

    return party_dict


def main():
    input_list = []
    with open("input.txt", "r") as doc:
        for line in doc:
            party, result = line.rsplit(maxsplit=1)
            input_list.append([party, int(result)])

    dictionary = func(input_list)
    for party in input_list:
        print(party[0], dictionary[party[0]])

def test():
    test_input_1 = [['Party One', 100000], ['Party Two', 200000], ['Party Three', 400000]]
    test_input_2 = [['Party One', 6], ['Party Two', 3], ['Party Three', 4]]
    test_input_3 = [['Party number one', 449], ['Partytwo', 1]]
    assert func(test_input_1) == {'Party Two': 129, 'Party One': 64, 'Party Three': 257}
    assert func(test_input_2) == {'Party Two': 104, 'Party One': 208, 'Party Three': 138}
    assert func(test_input_3) == {'Party number one': 449, 'Partytwo': 1}

if __name__ == '__main__':
    main()