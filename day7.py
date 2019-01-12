
import re
from collections import defaultdict, deque
import sys
import heapq

input="""Step E must be finished before step Y can begin.
Step Y must be finished before step T can begin.
Step I must be finished before step C can begin.
Step G must be finished before step F can begin.
Step C must be finished before step P can begin.
Step B must be finished before step Q can begin.
Step Z must be finished before step N can begin.
Step J must be finished before step W can begin.
Step W must be finished before step P can begin.
Step K must be finished before step D can begin.
Step Q must be finished before step L can begin.
Step V must be finished before step D can begin.
Step O must be finished before step M can begin.
Step A must be finished before step P can begin.
Step M must be finished before step L can begin.
Step R must be finished before step S can begin.
Step D must be finished before step X can begin.
Step X must be finished before step N can begin.
Step P must be finished before step T can begin.
Step F must be finished before step N can begin.
Step S must be finished before step L can begin.
Step U must be finished before step N can begin.
Step T must be finished before step L can begin.
Step N must be finished before step H can begin.
Step L must be finished before step H can begin.
Step N must be finished before step L can begin.
Step X must be finished before step F can begin.
Step P must be finished before step F can begin.
Step P must be finished before step H can begin.
Step B must be finished before step D can begin.
Step V must be finished before step H can begin.
Step X must be finished before step S can begin.
Step Q must be finished before step O can begin.
Step Z must be finished before step T can begin.
Step K must be finished before step N can begin.
Step S must be finished before step H can begin.
Step M must be finished before step P can begin.
Step Q must be finished before step D can begin.
Step R must be finished before step U can begin.
Step J must be finished before step P can begin.
Step P must be finished before step S can begin.
Step V must be finished before step U can begin.
Step R must be finished before step T can begin.
Step F must be finished before step S can begin.
Step D must be finished before step T can begin.
Step E must be finished before step N can begin.
Step J must be finished before step N can begin.
Step J must be finished before step A can begin.
Step K must be finished before step U can begin.
Step V must be finished before step N can begin.
Step V must be finished before step S can begin.
Step U must be finished before step L can begin.
Step F must be finished before step U can begin.
Step I must be finished before step T can begin.
Step J must be finished before step L can begin.
Step E must be finished before step T can begin.
Step T must be finished before step N can begin.
Step I must be finished before step G can begin.
Step R must be finished before step D can begin.
Step E must be finished before step B can begin.
Step X must be finished before step H can begin.
Step P must be finished before step L can begin.
Step Z must be finished before step J can begin.
Step O must be finished before step L can begin.
Step E must be finished before step H can begin.
Step F must be finished before step T can begin.
Step A must be finished before step F can begin.
Step U must be finished before step H can begin.
Step F must be finished before step H can begin.
Step C must be finished before step W can begin.
Step A must be finished before step L can begin.
Step V must be finished before step M can begin.
Step U must be finished before step T can begin.
Step E must be finished before step P can begin.
Step Y must be finished before step U can begin.
Step W must be finished before step R can begin.
Step E must be finished before step X can begin.
Step Q must be finished before step U can begin.
Step I must be finished before step F can begin.
Step V must be finished before step F can begin.
Step V must be finished before step T can begin.
Step R must be finished before step P can begin.
Step B must be finished before step A can begin.
Step S must be finished before step T can begin.
Step M must be finished before step F can begin.
Step Y must be finished before step F can begin.
Step C must be finished before step K can begin.
Step D must be finished before step S can begin.
Step O must be finished before step S can begin.
Step M must be finished before step U can begin.
Step Z must be finished before step S can begin.
Step R must be finished before step H can begin.
Step C must be finished before step O can begin.
Step G must be finished before step Q can begin.
Step Z must be finished before step D can begin.
Step B must be finished before step N can begin.
Step I must be finished before step H can begin.
Step I must be finished before step P can begin.
Step E must be finished before step J can begin.
Step V must be finished before step L can begin.
Step B must be finished before step U can begin.""".split("\n")

# input = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin.""".split("\n")

steps = [re.match("Step ([A-Z]) must be finished before step ([A-Z]) can begin.", l).groups() for l in input]

def get_prerequisits():
  prerequisits = defaultdict(list)
  for s in steps:
    prerequisits[s[1]].append(s[0])
    prerequisits[s[0]]
    prerequisits[s[1]]
  return sorted([[k, set(v)] for k, v in prerequisits.items()])


def part1(prerequisits):
  completed = set()
  print("Part 1: ", end="")
  while prerequisits:
      for i in range(0, len(prerequisits)):
        prerequisits[i][1] = prerequisits[i][1] - completed
        if not prerequisits[i][1]:
            completed.add(prerequisits[i][0])
            print(prerequisits[i][0], end="")
            del prerequisits[i]
            break
  print("")


def part2(prerequisits):
    workers = 5
    completed = set()
    completions = []
    time = 0
    
    print("Part 2: ", end="")

    while prerequisits or completions:
        if len(completions) == workers:
            time = completions[0][0]

        if completions and time >= completions[0][0]:
            t, finished = heapq.heappop(completions)
            completed.add(finished)
            print(finished, end="")
          
        for i in range(0, len(prerequisits)):
            prerequisits[i][1] = prerequisits[i][1] - completed
            if not prerequisits[i][1]:
                delay = 60 + ord(prerequisits[i][0]) - ord('A') + 1
                heapq.heappush(completions, (time + delay, prerequisits[i][0]))
                #print("{} started at {}".format(prerequisits[i][0], time))
                del prerequisits[i]
                break
        else:
            # nothing enqueued, better advance time to complete the next thing
            if completions:
                time = completions[0][0]

    print(" - time: {}".format(time))

part1(get_prerequisits())
part2(get_prerequisits())

