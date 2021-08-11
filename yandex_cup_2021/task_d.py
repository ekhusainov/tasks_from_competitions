import sys


def read_data():
    data = sys.stdin.read().split('\n')
    games_number = int(data[0])
    players = data[1:-1]
    return games_number, players


def check_two_degree(number):
    if number == 1:
        return True
    if number & 1:
        return False
    return check_two_degree(number >> 1)


def main():
    games_number, players = read_data()
    print(games_number)
    print(players)


if __name__ == "__main__":
    main()
