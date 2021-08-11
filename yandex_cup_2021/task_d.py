from collections import defaultdict
import sys
from typing import List, Dict, Tuple


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


def main():
    games_number, players = read_data()
    print(games_number)
    print(players)


if __name__ == "__main__":
    main()
