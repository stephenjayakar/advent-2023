"""Determine which games would have been possible if the bag had been
loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What
is the sum of the IDs of those games?

e.g.
Game 1: 4 green, 3 blue, 11 red; 7 red, 5 green, 10 blue; 3 green, 8 blue, 8 red; 4 red, 12 blue; 15 red, 3 green, 10 blue
"""

from functools import reduce

class Game:
    # string is of the form
    # "Game X: {# color,+};+
    def __init__(self, string: str):
        _, rest = string.split(': ')
        # processing "4 green, 3 blue,...; ..."
        rounds = rest.split('; ')
        self.rounds = []
        for round in rounds:
            round = round.strip()
            round_mapping = {}
            # processing "4 green, 3 blue..."
            colors = round.split(', ')
            for color_and_count in colors:
                # processing "4 green"
                number, color = color_and_count.split(' ')
                number = int(number)
                round_mapping[color] = number;
            self.rounds.append(round_mapping)

def game_test():
    tempStr = "Game 1: 4 green, 3 blue, 11 red; 7 red, 5 green, 10 blue; 3 green, 8 blue, 8 red; 4 red, 12 blue; 15 red, 3 green, 10 blue"
    g = Game(tempStr)
    print(tempStr)
    print(g.rounds)

def part_1(games):
    resources = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    valid_ids = []
    for i, game in enumerate(games):
        game_id = i + 1
        failed_round = False
        for resource, amount in resources.items():
            # reminder: this is with replacement
            for round in game.rounds:
                used = round.get(resource, 0)
                if used > amount:
                    failed_round = True
                    break
        if not failed_round:
            valid_ids.append(game_id)
    answer = sum(valid_ids)
    # print(valid_ids)
    # print(answer)
    # print(2 in valid_ids)
    return answer

def part_2(games):
    powers = []
    for game in games:
        maxes = {'red': 0, 'blue': 0, 'green': 0}
        for round in game.rounds:
            for color, amount in round.items():
                if maxes[color] < amount:
                    maxes[color] = amount
        power = reduce(lambda x, y: x * y, maxes.values())
        powers.append(power)
    return sum(powers)


games = []
with open('inputs/2', 'r') as file:
    lines = file.readlines()
for line in lines:
    games.append(Game(line))
print(part_1(games))
print(part_2(games))

