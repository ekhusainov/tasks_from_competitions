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
    games_number, players = read_data()
    power_2 = int(log2(games_number + 1))
    pairs = number_of_players_to_olympic_couple(power_2)
    generatic_players = list_tuple_to_list_str(pairs)
    etalon_answer = data_and_dict_to_sorted_frequency_count(
        generatic_players,
        building_dictionary_from_names(generatic_players)
    )
    dict_playes = building_dictionary_from_names(players)
    current_answer = data_and_dict_to_sorted_frequency_count(
        players,
        dict_playes,
    )
    if etalon_answer == current_answer:
        list_dict_playes = dict_playes.items()
        answer = [i[0] for i in list_dict_playes if i[1] == power_2]
        if check_data_for_double_name(players):
            print("NO SOLUTION")
        else:
            print(*answer)
    else:
        print("NO SOLUTION")


if __name__ == "__main__":
    main()
