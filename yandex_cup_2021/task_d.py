from collections import defaultdict
import sys
from typing import List, Dict, Tuple
from math import log2


def read_data() -> Tuple[int, List[str]]:
    data = sys.stdin.read().split('\n')
    games_number = int(data[0])
    players = data[1:-1]
    return games_number, players


def check_two_degree(number: int) -> bool:
    if number == 1:
        return True
    if number & 1:
        return False
    return check_two_degree(number >> 1)


def building_dictionary_from_names(data_names: List[str]) -> Dict[str, int]:
    name_frequency = defaultdict(int)
    for current_two_names in data_names:
        name1, name2 = current_two_names.split()
        name_frequency[name1] += 1
        name_frequency[name2] += 1
    return name_frequency


def list_strings_to_list_list_strings(data_names):
    return [i.split() for i in data_names]


def check_to_correct(data_list_list_string, data_dict, begin_stage):
    current_arr = data_list_list_string.copy()
    power_2 = int(log2(begin_stage))
    for stage_number in range(1, power_2 + 1):
        number_of_delete = 0
        list_for_delete = []
        for name1, name2 in current_arr:
            if data_dict[name1] == stage_number or data_dict[name2] == stage_number:
                list_for_delete.append([name1, name2])
                number_of_delete += 1

        if number_of_delete != begin_stage:
            return False
        for name1, name2 in list_for_delete:
            current_arr.remove([name1, name2])
        begin_stage = begin_stage // 2
    name1, name2 = current_arr[0]
    stage_number += 1
    if data_dict[name1] == stage_number or data_dict[name2] == stage_number:
        return current_arr
    return False


def data_and_dict_to_sorted_frequency_count(data_names: List[str],
                                            name_frequency: Dict[str, int])\
        -> List[Tuple[int]]:
    name_frequency_data = []
    for current_two_names in data_names:
        name1, name2 = current_two_names.split()
        freq1 = name_frequency[name1]
        freq2 = name_frequency[name2]
        name_frequency_data.append((min(freq1, freq2), max(freq1, freq2)))
    name_frequency_data = sorted(name_frequency_data)
    return name_frequency_data


def number_of_players_to_olympic_couple(number: int) -> List[Tuple[int]]:
    range_list = list(range(1, 2 ** number + 1))
    pairs = []
    for i in range(number):
        current_pairs = list(zip(range_list[0::2], range_list[1::2]))
        for j in current_pairs:
            pairs.append(j)
        range_list = [i[0] for i in current_pairs]
    return pairs


def list_tuple_to_list_str(pairs):
    return [str(i[0]) + " " + str(i[1]) for i in pairs]


def check_data_for_double_name(data_names):
    for current_two_names in data_names:
        name1, name2 = current_two_names.split()
        if name1 == name2:
            return True
    return False


def main():
    # data_names = [
    #     "9 11",
    #     "5 6",
    #     "1 9",
    #     "9 10",
    #     "15 16",
    #     "13 15",
    #     "3 4",
    #     "1 2",
    #     "7 8",
    #     "1 3",
    #     "13 14",
    #     "1 5",
    #     "9 13",
    #     "11 12",
    #     "5 7",
    # ]
    # data_list_list  = list_strings_to_list_list_strings(data_names)
    # data_dict = building_dictionary_from_names(data_names)
    # ans = check_to_correct(data_list_list, data_dict, 8)
    # print(ans)
    games_number, players = read_data()
    begin_stage = (games_number + 1) // 2
    data_list_list = list_strings_to_list_list_strings(players)
    data_dict = building_dictionary_from_names(players)
    ans = check_to_correct(data_list_list, data_dict, begin_stage)
    if not ans:
        print("NO SOLUTION")
    else:
        print(*ans[0])
    # power_2 = int(log2(games_number + 1))
    # pairs = number_of_players_to_olympic_couple(power_2)
    # generatic_players = list_tuple_to_list_str(pairs)
    # etalon_answer = data_and_dict_to_sorted_frequency_count(
    #     generatic_players,
    #     building_dictionary_from_names(generatic_players)
    # )
    # dict_playes = building_dictionary_from_names(players)
    # current_answer = data_and_dict_to_sorted_frequency_count(
    #     players,
    #     dict_playes,
    # )
    # if etalon_answer == current_answer:
    #     list_dict_playes = dict_playes.items()
    #     answer = [i[0] for i in list_dict_playes if i[1] == power_2]
    #     if check_data_for_double_name(players):
    #         print("NO SOLUTION")
    #     else:
    #         print(*answer)
    # else:
    #     print("NO SOLUTION")


if __name__ == "__main__":
    main()
