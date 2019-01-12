#!/usr/bin/env python3.6

import re
import random

# input = """position=< 9,  1> velocity=< 0,  2>
# position=< 7,  0> velocity=<-1,  0>
# position=< 3, -2> velocity=<-1,  1>
# position=< 6, 10> velocity=<-2, -1>
# position=< 2, -4> velocity=< 2,  2>
# position=<-6, 10> velocity=< 2, -2>
# position=< 1,  8> velocity=< 1, -1>
# position=< 1,  7> velocity=< 1,  0>
# position=<-3, 11> velocity=< 1, -2>
# position=< 7,  6> velocity=<-1, -1>
# position=<-2,  3> velocity=< 1,  0>
# position=<-4,  3> velocity=< 2,  0>
# position=<10, -3> velocity=<-1,  1>
# position=< 5, 11> velocity=< 1, -2>
# position=< 4,  7> velocity=< 0, -1>
# position=< 8, -2> velocity=< 0,  1>
# position=<15,  0> velocity=<-2,  0>
# position=< 1,  6> velocity=< 1,  0>
# position=< 8,  9> velocity=< 0, -1>
# position=< 3,  3> velocity=<-1,  1>
# position=< 0,  5> velocity=< 0, -1>
# position=<-2,  2> velocity=< 2,  0>
# position=< 5, -2> velocity=< 1,  2>
# position=< 1,  4> velocity=< 2,  1>
# position=<-2,  7> velocity=< 2, -2>
# position=< 3,  6> velocity=<-1, -1>
# position=< 5,  0> velocity=< 1,  0>
# position=<-6,  0> velocity=< 2,  0>
# position=< 5,  9> velocity=< 1, -2>
# position=<14,  7> velocity=<-2,  0>
# position=<-3,  6> velocity=< 2, -1>""".split("\n")

input = """position=< 31766, -52454> velocity=<-3,  5>
position=<-52374, -41935> velocity=< 5,  4>
position=< 31758, -31427> velocity=<-3,  3>
position=<-41862,  31671> velocity=< 4, -3>
position=< 10747, -41934> velocity=<-1,  4>
position=< 21267,  42181> velocity=<-2, -4>
position=< 52759, -20913> velocity=<-5,  2>
position=< 31734,  52701> velocity=<-3, -5>
position=<-41823,  31669> velocity=< 4, -3>
position=<-52346,  42184> velocity=< 5, -4>
position=<-20801, -52451> velocity=< 2,  5>
position=< 31760, -20904> velocity=<-3,  2>
position=<-31356, -10397> velocity=< 3,  1>
position=<-41823, -41934> velocity=< 4,  4>
position=< 10724, -10389> velocity=<-1,  1>
position=<-31344, -31427> velocity=< 3,  3>
position=<-41826,  42186> velocity=< 4, -4>
position=<-52393,  42186> velocity=< 5, -4>
position=< 42281,  52698> velocity=<-4, -5>
position=< 10700, -10398> velocity=<-1,  1>
position=< 21259,  31667> velocity=<-2, -3>
position=< 21215,  31662> velocity=<-2, -3>
position=<-10294,  10635> velocity=< 1, -1>
position=< 31734, -10392> velocity=<-3,  1>
position=< 52764,  52698> velocity=<-5, -5>
position=<-52394,  21148> velocity=< 5, -2>
position=<-20809, -31428> velocity=< 2,  3>
position=<-52333,  31666> velocity=< 5, -3>
position=< 31787, -20913> velocity=<-3,  2>
position=< 52776, -10391> velocity=<-5,  1>
position=<-52393, -52449> velocity=< 5,  5>
position=< 31768,  52701> velocity=<-3, -5>
position=< 31734,  21155> velocity=<-3, -2>
position=<-41847, -52455> velocity=< 4,  5>
position=< 21220,  21147> velocity=<-2, -2>
position=< 42273,  10640> velocity=<-4, -1>
position=< 10753,  52696> velocity=<-1, -5>
position=<-10309, -10389> velocity=< 1,  1>
position=< 42241,  21149> velocity=<-4, -2>
position=< 52806,  52701> velocity=<-5, -5>
position=<-20801,  31670> velocity=< 2, -3>
position=< 10720,  21152> velocity=<-1, -2>
position=< 31737,  42181> velocity=<-3, -4>
position=<-31332, -20913> velocity=< 3,  2>
position=<-10321,  52695> velocity=< 1, -5>
position=<-10294,  31664> velocity=< 1, -3>
position=<-10331, -41943> velocity=< 1,  4>
position=< 52788, -10397> velocity=<-5,  1>
position=< 52766, -31428> velocity=<-5,  3>
position=<-31332, -52458> velocity=< 3,  5>
position=<-31356, -20909> velocity=< 3,  2>
position=<-10329, -52453> velocity=< 1,  5>
position=<-31346, -31419> velocity=< 3,  3>
position=< 31787,  10638> velocity=<-3, -1>
position=< 10736,  21152> velocity=<-1, -2>
position=< 21255, -31419> velocity=<-2,  3>
position=<-31308,  31669> velocity=< 3, -3>
position=<-52386,  42186> velocity=< 5, -4>
position=<-10314, -20912> velocity=< 1,  2>
position=< 31766, -41938> velocity=<-3,  4>
position=< 42273,  21149> velocity=<-4, -2>
position=< 21255, -31419> velocity=<-2,  3>
position=<-41860, -41934> velocity=< 4,  4>
position=<-20817, -31421> velocity=< 2,  3>
position=< 21231,  52695> velocity=<-2, -5>
position=<-20793,  21151> velocity=< 2, -2>
position=< 42274,  31671> velocity=<-4, -3>
position=<-31353,  10636> velocity=< 3, -1>
position=< 21235, -41937> velocity=<-2,  4>
position=< 21251, -52452> velocity=<-2,  5>
position=< 42289, -20905> velocity=<-4,  2>
position=< 52766,  31666> velocity=<-5, -3>
position=<-52357,  52701> velocity=< 5, -5>
position=<-52386, -41935> velocity=< 5,  4>
position=< 42260, -20913> velocity=<-4,  2>
position=<-20836,  42180> velocity=< 2, -4>
position=<-52386,  31670> velocity=< 5, -3>
position=< 10757, -10390> velocity=<-1,  1>
position=< 10752,  42183> velocity=<-1, -4>
position=<-52381,  10633> velocity=< 5, -1>
position=<-31332,  31667> velocity=< 3, -3>
position=< 21237,  52701> velocity=<-2, -5>
position=< 10731, -41934> velocity=<-1,  4>
position=< 31787, -31425> velocity=<-3,  3>
position=< 52757, -41943> velocity=<-5,  4>
position=<-52374,  52698> velocity=< 5, -5>
position=<-52338, -52456> velocity=< 5,  5>
position=<-20844,  42178> velocity=< 2, -4>
position=<-20825, -52456> velocity=< 2,  5>
position=<-52367, -10389> velocity=< 5,  1>
position=< 10744,  52697> velocity=<-1, -5>
position=< 10704, -52457> velocity=<-1,  5>
position=< 31766,  42186> velocity=<-3, -4>
position=< 52761, -10390> velocity=<-5,  1>
position=< 31777, -20904> velocity=<-3,  2>
position=<-41818, -41938> velocity=< 4,  4>
position=<-52370,  10637> velocity=< 5, -1>
position=< 21267,  10639> velocity=<-2, -1>
position=<-52382, -10394> velocity=< 5,  1>
position=<-52370,  42180> velocity=< 5, -4>
position=< 21223, -31428> velocity=<-2,  3>
position=<-20845, -20913> velocity=< 2,  2>
position=< 52812,  21148> velocity=<-5, -2>
position=< 42241, -41935> velocity=<-4,  4>
position=< 52814,  52696> velocity=<-5, -5>
position=<-31316, -10398> velocity=< 3,  1>
position=< 52776,  10636> velocity=<-5, -1>
position=<-41823,  21148> velocity=< 4, -2>
position=< 52788, -10391> velocity=<-5,  1>
position=<-52370,  42186> velocity=< 5, -4>
position=< 10721,  52701> velocity=<-1, -5>
position=< 10744,  42185> velocity=<-1, -4>
position=< 21219, -41939> velocity=<-2,  4>
position=<-52378, -52451> velocity=< 5,  5>
position=< 31758, -20911> velocity=<-3,  2>
position=<-31332,  52697> velocity=< 3, -5>
position=<-10329,  31671> velocity=< 1, -3>
position=<-31308,  42179> velocity=< 3, -4>
position=< 31726, -20911> velocity=<-3,  2>
position=< 42275,  52701> velocity=<-4, -5>
position=<-20829,  21149> velocity=< 2, -2>
position=< 10706,  52696> velocity=<-1, -5>
position=<-31312,  52701> velocity=< 3, -5>
position=<-31364, -10397> velocity=< 3,  1>
position=<-41855,  42179> velocity=< 4, -4>
position=<-41823,  31665> velocity=< 4, -3>
position=<-31362, -10389> velocity=< 3,  1>
position=< 42273, -20912> velocity=<-4,  2>
position=< 10700, -52453> velocity=<-1,  5>
position=< 52788,  21149> velocity=<-5, -2>
position=<-10324, -31424> velocity=< 1,  3>
position=<-31356, -31423> velocity=< 3,  3>
position=< 10725,  52701> velocity=<-1, -5>
position=<-52343,  42186> velocity=< 5, -4>
position=<-31324, -31425> velocity=< 3,  3>
position=< 52799, -31419> velocity=<-5,  3>
position=< 10716, -52458> velocity=<-1,  5>
position=<-20849,  10638> velocity=< 2, -1>
position=<-52378, -20905> velocity=< 5,  2>
position=< 52764, -10391> velocity=<-5,  1>
position=< 31726,  10635> velocity=<-3, -1>
position=< 31750, -20907> velocity=<-3,  2>
position=<-31344,  10636> velocity=< 3, -1>
position=<-41839, -10397> velocity=< 4,  1>
position=<-52333,  52701> velocity=< 5, -5>
position=< 52780, -41939> velocity=<-5,  4>
position=< 42242,  10641> velocity=<-4, -1>
position=< 10728, -20909> velocity=<-1,  2>
position=< 52780, -41943> velocity=<-5,  4>
position=< 31766, -41939> velocity=<-3,  4>
position=<-20846, -41934> velocity=< 2,  4>
position=<-31303,  10640> velocity=< 3, -1>
position=< 42282, -41934> velocity=<-4,  4>
position=< 52780, -20907> velocity=<-5,  2>
position=< 31726, -20908> velocity=<-3,  2>
position=<-10310,  31666> velocity=< 1, -3>
position=<-31316, -41940> velocity=< 3,  4>
position=<-20801,  10635> velocity=< 2, -1>
position=<-41859, -10396> velocity=< 4,  1>
position=< 31750,  31669> velocity=<-3, -3>
position=<-52370,  21151> velocity=< 5, -2>
position=<-31312, -52449> velocity=< 3,  5>
position=<-20821, -10389> velocity=< 2,  1>
position=< 10744,  42179> velocity=<-1, -4>
position=< 31766, -20909> velocity=<-3,  2>
position=<-41870,  52692> velocity=< 4, -5>
position=<-52366,  31671> velocity=< 5, -3>
position=<-31364, -41938> velocity=< 3,  4>
position=<-31324,  52700> velocity=< 3, -5>
position=< 42289, -52449> velocity=<-4,  5>
position=<-10298,  21156> velocity=< 1, -2>
position=< 21212,  31662> velocity=<-2, -3>
position=< 10696, -20907> velocity=<-1,  2>
position=< 52776,  52699> velocity=<-5, -5>
position=< 42261,  52697> velocity=<-4, -5>
position=< 21235, -20905> velocity=<-2,  2>
position=<-52334,  42181> velocity=< 5, -4>
position=< 52777, -31428> velocity=<-5,  3>
position=< 10716,  31665> velocity=<-1, -3>
position=< 52817, -41943> velocity=<-5,  4>
position=< 52798, -41934> velocity=<-5,  4>
position=<-52338,  52696> velocity=< 5, -5>
position=<-52338,  42178> velocity=< 5, -4>
position=< 31787,  42186> velocity=<-3, -4>
position=<-31356, -52454> velocity=< 3,  5>
position=< 21259,  31667> velocity=<-2, -3>
position=<-20807,  10641> velocity=< 2, -1>
position=<-31319,  10641> velocity=< 3, -1>
position=< 31746,  31667> velocity=<-3, -3>
position=<-31324,  31671> velocity=< 3, -3>
position=<-10278, -10398> velocity=< 1,  1>
position=<-10286,  42181> velocity=< 1, -4>
position=< 42257, -10390> velocity=<-4,  1>
position=<-52354,  10641> velocity=< 5, -1>
position=<-20845, -31423> velocity=< 2,  3>
position=< 21220, -31424> velocity=<-2,  3>
position=< 21230, -20904> velocity=<-2,  2>
position=<-52392, -41934> velocity=< 5,  4>
position=<-20793,  52694> velocity=< 2, -5>
position=< 10744, -41941> velocity=<-1,  4>
position=< 31758,  42185> velocity=<-3, -4>
position=<-20788,  21149> velocity=< 2, -2>
position=<-52346, -31428> velocity=< 5,  3>
position=< 31729, -20908> velocity=<-3,  2>
position=< 52804, -20909> velocity=<-5,  2>
position=<-20841,  52697> velocity=< 2, -5>
position=<-20820, -41934> velocity=< 2,  4>
position=<-20829, -41936> velocity=< 2,  4>
position=<-52375,  10632> velocity=< 5, -1>
position=<-41874,  42184> velocity=< 4, -4>
position=< 52756,  52700> velocity=<-5, -5>
position=< 42265,  42184> velocity=<-4, -4>
position=<-31364,  31668> velocity=< 3, -3>
position=<-10310,  42178> velocity=< 1, -4>
position=< 10716, -52454> velocity=<-1,  5>
position=< 31774, -41937> velocity=<-3,  4>
position=<-52389,  10638> velocity=< 5, -1>
position=< 31747,  52692> velocity=<-3, -5>
position=<-31316, -52457> velocity=< 3,  5>
position=< 52760, -31423> velocity=<-5,  3>
position=<-31305,  21151> velocity=< 3, -2>
position=< 10736, -31421> velocity=<-1,  3>
position=<-10326,  10634> velocity=< 1, -1>
position=<-41847, -20905> velocity=< 4,  2>
position=<-10286,  31666> velocity=< 1, -3>
position=< 31787, -20906> velocity=<-3,  2>
position=< 42290, -31419> velocity=<-4,  3>
position=< 21223, -10394> velocity=<-2,  1>
position=<-31306, -10394> velocity=< 3,  1>
position=<-20801,  21149> velocity=< 2, -2>
position=< 31753, -52449> velocity=<-3,  5>
position=< 31787,  21151> velocity=<-3, -2>
position=<-10314,  10634> velocity=< 1, -1>
position=< 42284,  21156> velocity=<-4, -2>
position=< 21235,  10632> velocity=<-2, -1>
position=< 21228,  31671> velocity=<-2, -3>
position=<-20825,  21147> velocity=< 2, -2>
position=< 31758,  21153> velocity=<-3, -2>
position=<-31305, -20909> velocity=< 3,  2>
position=< 42241,  42184> velocity=<-4, -4>
position=<-20801,  31663> velocity=< 2, -3>
position=< 52796, -52453> velocity=<-5,  5>
position=<-10334, -31423> velocity=< 1,  3>
position=< 52764, -31425> velocity=<-5,  3>
position=< 10720, -10393> velocity=<-1,  1>
position=<-20844, -31422> velocity=< 2,  3>
position=< 10704,  10635> velocity=<-1, -1>
position=< 42250,  52696> velocity=<-4, -5>
position=<-10273,  52695> velocity=< 1, -5>
position=< 10698,  31662> velocity=<-1, -3>
position=<-10278,  10638> velocity=< 1, -1>
position=< 21211,  52693> velocity=<-2, -5>
position=< 42298, -31424> velocity=<-4,  3>
position=<-10326,  52701> velocity=< 1, -5>
position=< 31760,  31671> velocity=<-3, -3>
position=< 10752,  10641> velocity=<-1, -1>
position=<-10313, -10398> velocity=< 1,  1>
position=<-31311,  31671> velocity=< 3, -3>
position=< 42273, -31422> velocity=<-4,  3>
position=< 10720,  42184> velocity=<-1, -4>
position=<-20845,  31670> velocity=< 2, -3>
position=<-31347,  10641> velocity=< 3, -1>
position=<-10332,  52692> velocity=< 1, -5>
position=<-31332, -31419> velocity=< 3,  3>
position=< 42293,  21156> velocity=<-4, -2>
position=<-31353,  10632> velocity=< 3, -1>
position=<-31316,  52699> velocity=< 3, -5>
position=<-31364,  21149> velocity=< 3, -2>
position=<-10278,  21156> velocity=< 1, -2>
position=< 42302, -31427> velocity=<-4,  3>
position=< 21219, -41942> velocity=<-2,  4>
position=< 31731,  52701> velocity=<-3, -5>
position=< 42241, -20909> velocity=<-4,  2>
position=<-31344, -10397> velocity=< 3,  1>
position=< 42277, -20904> velocity=<-4,  2>
position=<-10274, -41939> velocity=< 1,  4>
position=< 31782, -52450> velocity=<-3,  5>
position=<-41876,  31667> velocity=< 4, -3>
position=< 10749, -20904> velocity=<-1,  2>
position=< 21224, -20911> velocity=<-2,  2>
position=< 31734,  31662> velocity=<-3, -3>
position=< 21231,  10635> velocity=<-2, -1>
position=<-52389, -31419> velocity=< 5,  3>
position=< 31734, -41937> velocity=<-3,  4>
position=< 42257, -20905> velocity=<-4,  2>
position=< 42297,  52697> velocity=<-4, -5>
position=< 52805,  21156> velocity=<-5, -2>
position=< 10709, -20910> velocity=<-1,  2>
position=<-52370, -31420> velocity=< 5,  3>
position=<-10326,  21152> velocity=< 1, -2>""".split("\n")

def parse_line(line):
    x, y, dx, dy = re.match(
        "position=<([ 0-9-]+), ([ 0-9-]+)> velocity=<([ 0-9-]+), ([ 0-9-]+)>", 
        line
        ).groups()
    return (int(x), int(y), int(dx), int(dy))


coords = [parse_line(line) for line in input]


def get_coords_around(coords, coord):
    return [
        c 
        for c in coords
        if abs(c[0]-coord[0]) <= 1 and 
            abs(c[1]-coord[1]) <= 1 and 
            (c[1] != coord[1] or c[0] != coord[0])
        ]

def walk(coords, coord, acc, visitneighbours):
    if len(acc) > visitneighbours:
        return True
    around = get_coords_around(coords, coord)
    around = [a for a in around if a not in acc]
    if len(around) < 1:
        return False
    else:
        for a in around:
            acc.add(a)
        return all([
            walk(coords, a, acc, visitneighbours) 
            for a in around
            ])
    

def isgood(coords, visitneighbours):
    # pick 3 random points and see if a random walk has at least visitneighbours
    if (
            walk(coords, random.choice(coords), set(), visitneighbours) and 
            walk(coords, random.choice(coords), set(), visitneighbours) and
            walk(coords, random.choice(coords), set(), visitneighbours)
            ):
        return True

print(
    "Warning, this is probablistic.  If an answer is not found in <10sec,"
    " try restarting it."
    )

iteration = 0
while True:
    if isgood(coords, 7):
        print("Iteration: {} OK".format(iteration))
        max_x = max(coords, key=lambda c: c[0])[0]
        min_x = min(coords, key=lambda c: c[0])[0]
        max_y = max(coords, key=lambda c: c[1])[1]
        min_y = min(coords, key=lambda c: c[1])[1]

        rowsize = (max_x - min_x + 1)
        colsize = (max_y - min_y + 1)
        chart = ['.'] * (rowsize * colsize)
        for x, y, dx, dy in coords:
            xpos = x - min_x
            ypos = y - min_y
            try:
                chart[xpos + (ypos * rowsize)] = '#'
            except:
                import pdb; pdb.set_trace()
        print("Part 1: ")
        for row in range(0, colsize):
            print(" ".join(chart[(row * rowsize):((row + 1) * rowsize)]))
        print("Part 2: {}".format(iteration))
        break

    coords = [(x + dx, y + dy, dx, dy) for x, y, dx, dy in coords]
    iteration += 1