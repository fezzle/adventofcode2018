import re
from itertools import cycle

input = (
    """10 players; last marble is worth 1618 points: high score is 8317
13 players; last marble is worth 7999 points: high score is 146373
17 players; last marble is worth 1104 points: high score is 2764
21 players; last marble is worth 6111 points: high score is 54718
30 players; last marble is worth 5807 points: high score is 37305
441 players; last marble is worth 71032 points: high score is 00
441 players; last marble is worth 7103200 points: high score is 00""").split("\n")


matcher = re.compile("([0-9]+) players; last marble is worth ([0-9]+) points: high score is ([0-9]+)")

def get_top_score(line):
    player_count, points, high_score = matcher.match(line).groups()
    player_count = int(player_count)
    points = int(points)

    class Player(object):
        def __init__(self, id):
            self.id = id
            self.score = 0

        def inc_score(self, inc):
            self.score += inc


    class Marble(object):
        current_marble = None

        def __init__(self, player, counter):
            self.player = player
            self.counter = counter

            if counter == 0:
                assert Marble.current_marble is None
                Marble.current_marble = self
                self.left = Marble.current_marble
                self.right = Marble.current_marble
            elif (counter % 23) == 0:
                self.player.inc_score(counter)
                to_rem = Marble.current_marble.left.left.left.left.left.left.left 
                to_rem.left.right = to_rem.right
                to_rem.right.left = to_rem.left
                self.player.inc_score(to_rem.counter)
                Marble.current_marble = to_rem.right
            else:
                self.left = Marble.current_marble.right
                self.right = Marble.current_marble.right.right
                self.left.right = self
                self.right.left = self
                Marble.current_marble = self            
        
    players = [Player(i) for i in range(0, player_count)]
    for p, i in zip(cycle(players), range(0, points + 1)):
        Marble(p, i) 
    return max(players, key=lambda p: p.score).score


print("Part 1: {}".format(get_top_score(input[5])))
print("Part 2: {}".format(get_top_score(input[6])))
