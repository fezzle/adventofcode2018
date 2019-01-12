import sys
from collections import deque

input = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######""".split("\n")  # expect: 47 * 590 = 27730

input = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######""".split("\n")  # expect 37 * 982 = 36334


input = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######""".split("\n") # expect 46 * 859 = 39514


input = """#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######""".split("\n") #  expect 35 * 793 = 27755

input = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######""".split("\n") #  54 * 536 = 28944

input = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########""".split("\n")  #  20 * 937 = 18740

input = """################################
####################.###########
###################..##..#######
###################.###..#######
###################.###.########
##################G.###.########
##..############.#..##..########
#...#####.####.....##...########
#G.....##..###.#.GG#...G.....G##
#...G....G.G##.....#.#.......###
##..............G............###
#......GG.....G............#####
#####.........#####.......E..###
#####.....G..#######.......#####
#####.......#########......###.#
######......#########..........#
#####.....G.#########..........#
##.....#...G#########......#...#
###.#....G..#########G.........#
##..###......#######E..........#
##..###...G...#####E..E.....E..#
###..##...............E.#.E....#
###..##..##E...###......##..####
##..G...###....###......########
##......###E....##....##########
###...#####..E..###...##########
##....####......####.###########
####..#####.....##...###########
############..####....##########
############.#####....##########
##########...#####.#.###########
################################""".split("\n")

width = len(input[0]) 
height = len(input)

class Elf(object):
    char = 'E'
    def __init__(self):
        self.hit_points = 200
        self.last_turn = -1

class Goblin(object):
    char = 'G'
    def __init__(self):
        self.hit_points = 200
        self.last_turn = -1

class Wall(object):
    _instance = None
    char = '#'
    def __new__(cls):
        cls._instance = cls._instance or super(Wall, cls).__new__(cls)
        return cls._instance

class Empty(object):  # singleton 
    _instance = None
    char = '.'
    def __new__(cls):
        cls._instance = cls._instance or super(Empty, cls).__new__(cls)
        return cls._instance

def make_cell(c):
    return {
        Goblin.char: Goblin,
        Elf.char: Elf,
        Wall.char: Wall,
        Empty.char: Empty,
        }[c]()

def i_up(i):
    x, y = i_to_c(i)
    assert(y > 0)
    return x + (y-1)*width

def i_down(i):
    x, y = i_to_c(i)
    assert(y < height - 1)
    return x + (y+1)*width

def i_left(i):
    x, y = i_to_c(i)
    assert(x > 0)
    return (x - 1) + y*width

def i_right(i):
    x, y = i_to_c(i)
    assert(x < width)
    return (x + 1) + y*width

def i_to_c(i):
    return (i % width, int(i / width))  

def is_empty(cell):
    return isinstance(cell, Empty)

def is_wall(cell):
    return isinstance(cell, Wall)

def is_goblin(cell):
    return isinstance(cell, Goblin)

def is_elf(cell):
    return isinstance(cell, Elf)

def get_surrounding_squares(chart, index, predicate=is_empty):
    if predicate(chart[i_up(index)]):
        yield i_up(index)
    if predicate(chart[i_left(index)]):
        yield i_left(index)
    if predicate(chart[i_right(index)]):
        yield i_right(index)
    if predicate(chart[i_down(index)]):
        yield i_down(index)

def print_state(label, c, w):
    print("***{}***".format(label))
    for j in range(0, int(len(c)/w)):
        for i in range(0, w):
            print(c[i + w*j].char, end="")
        print(
            "   {}".format(", ".join(
                [
                    "{}({})".format(c.char, c.hit_points) 
                    for c in c[w*j:w*(j+1)]
                    if is_elf(c) or is_goblin(c)
                    ])),
                    end="")
        print("")
    print("")


def get_reachability(chart, i1, i2, distance=0, steps=None):
    """
    :return: tuple of (distance, first_step) to i2
    """
    c2 = chart.copy()

    steps_to_explore = deque([(0, None, i1)])
    while steps_to_explore:
        distance_so_far, first_step, place = steps_to_explore.pop()
        if place == i2:
            return (distance_so_far, first_step)
        
        for next_step in get_surrounding_squares(c2, place, is_empty):
            c2[next_step] = Wall()
            steps_to_explore.appendleft(
                (distance_so_far + 1, first_step or next_step, next_step)
                )
    return False


def run_sim(chart, elf_hit_damage=3):
    elf_deaths = 0
    for turn_count in range(0, sys.maxsize):
        #print_state("After Round {}".format(turn_count), chart, width)

        for i, c in enumerate(chart):
            if is_empty(c) or is_wall(c):
                continue

            if c.last_turn == turn_count:
                # this critter already moved
                continue
            else:
                c.last_turn = turn_count

            is_enemy = is_goblin if isinstance(c, Elf) else is_elf
            hit_damage = elf_hit_damage if isinstance(c, Elf) else 3
            surrounding_enemies = [
                (chart[e].hit_points, e) for e in get_surrounding_squares(chart, i, is_enemy)
                ]
            
            if not surrounding_enemies:
                enemies = [i for i, e in enumerate(chart) if is_enemy(e)]
                squares_around_enemies = [
                    s 
                    for e in enemies 
                    for s in get_surrounding_squares(chart, e)
                    ]
                reachabilities = [
                    get_reachability(chart, i, s) for s in squares_around_enemies
                    ]
                reachabilities_filtered = [r for r in reachabilities if r is not False]
                reachabilities_by_closest = sorted(reachabilities_filtered)
                if not reachabilities_by_closest:
                    continue

                distance, first_step = reachabilities_by_closest[0]
                chart[i] = Empty()
                chart[first_step] = c
                i = first_step
                
                surrounding_enemies = [
                    (chart[e].hit_points, e) for e in get_surrounding_squares(chart, i, is_enemy)
                    ]
        
            if surrounding_enemies:
                surrounding_enemies_sorted = sorted(surrounding_enemies)
                enemy_hit_points, enemy_to_attack = surrounding_enemies_sorted[0]
                chart[enemy_to_attack].hit_points -= hit_damage
                if chart[enemy_to_attack].hit_points <= 0:
                    if is_elf(chart[enemy_to_attack]):
                        elf_deaths += 1

                    # print("{} dead at {},{}".format(
                    #     chart[enemy_to_attack].char, 
                    #     *i_to_c(i))
                    #     )
                    chart[enemy_to_attack] = Empty()
                    
                    elves_extant = any(map(is_elf, chart))
                    goblins_extant = any(map(is_goblin, chart))
                    # if not elves_extant:
                    #     print_state("Goblins win in round {}".format(turn_count+1), chart, width)
                    # elif not goblins_extant:
                    #     print_state("Elves win in round {}".format(turn_count+1), chart, width)

                    if not elves_extant or not goblins_extant:
                        total_hit_points = sum(
                            [c.hit_points for c in chart if is_goblin(c) or is_elf(c)]
                            )
                        print("Round:{}, Hit Points Remaining:{}, Outcome Score: {} or {})".format(
                            turn_count, 
                            total_hit_points, 
                            turn_count * total_hit_points, 
                            (turn_count+1)*total_hit_points
                            ))
                        return elf_deaths



elves_died = run_sim(
    chart=[make_cell(c) for line in input for c in line], 
    elf_hit_damage=3
    )
print("Part 1, {} elves died".format(elves_died))

damage_points = 3
while damage_points < 1000:
    damage_points += 1
    elves_died = run_sim(
        chart=[make_cell(c) for line in input for c in line],
        elf_hit_damage=damage_points
        )    
    print("Part 2, {} elves died with {} damage points".format(
        elves_died, damage_points
        ))