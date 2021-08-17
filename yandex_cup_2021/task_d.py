from collections import defaultdict
import sys
from typing import List, Dict, Tuple
from math import log2


def read_data() -> Tuple[int, List[str]]:
    data = sys.stdin.read().split('\n')
    games_number = int(data[0])
    players = data[1:-1]
    return games_number, players


def building_dictionary_from_names(data_names: List[str]) -> Dict[str, int]:
    name_frequency = defaultdict(int)
    for current_two_names in data_names:
        name1, name2 = current_two_names.split()
        name_frequency[name1] += 1
        name_frequency[name2] += 1
    return name_frequency


def list_strings_to_list_list_strings(data_names):
    return [i.split() for i in data_names]


def check_if_the_number_of_participants_is_correct(data_list_list_string, players_number):
    full_list_players = []
    for i in data_list_list_string:
        full_list_players.append(i[0])
        full_list_players.append(i[1])
    full_list_players = list(set(full_list_players))
    return len(full_list_players) == players_number


def check_to_correct(data_list_list_string, data_dict, begin_stage):
    if not check_if_the_number_of_participants_is_correct(data_list_list_string, begin_stage * 2):
        return False
    current_arr = data_list_list_string.copy()
    power_2 = int(log2(begin_stage))
    for stage_number in range(1, power_2 + 1):
        number_of_delete = 0
        list_for_delete = []
        for name1, name2 in current_arr:
            if data_dict[name1] == stage_number and data_dict[name2] == stage_number:
                return False
            if data_dict[name1] == stage_number or data_dict[name2] == stage_number:
                list_for_delete.append([name1, name2])
                number_of_delete += 1

        if number_of_delete != begin_stage:
            return False
        if stage_number == 1:
            if not check_if_the_number_of_participants_is_correct(list_for_delete, begin_stage * 2):
                return False
        for name1, name2 in list_for_delete:
            current_arr.remove([name1, name2])
        begin_stage = begin_stage // 2
    name1, name2 = current_arr[0]
    stage_number += 1
    if data_dict[name1] == stage_number or data_dict[name2] == stage_number:
        return current_arr
    return False


def main():
    games_number, players = read_data()
    begin_stage = (games_number + 1) // 2
    data_list_list = list_strings_to_list_list_strings(players)
    data_dict = building_dictionary_from_names(players)
    ans = check_to_correct(data_list_list, data_dict, begin_stage)
    if not ans:
        print("NO SOLUTION")
    else:
        print(*ans[0])


if __name__ == "__main__":
    main()
