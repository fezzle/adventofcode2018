

scores = [3, 7]

elf1 = 0
elf2 = 1

input = [int(c) for c in '190221']

done_part1 = False
done_part2 = False

def print_state():
    for i, n in enumerate(scores):
        prefix, postfix = ' ', ' '
        if i == elf1 and i == elf2:
            prefix, postfix = '{', '}'
        if i == elf1:
            prefix, postfix = '(', ')'
        if i == elf2:
            prefix, postfix = '[', ']'
        print("{}{}{}".format(prefix, n, postfix), end="")
    print("")

print_state()
while True:
    total = scores[elf1] + scores[elf2]
    tens = int(total / 10)
    if tens:
        scores.append(tens)
    scores.append(total % 10)

    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)

    #print_state()

    if not done_part2 and scores[-len(input):] == input:
        print("Part 2: {}".format(len(scores) - len(input)))
        if done_part1:
            break
        done_part2 = True

    if not done_part1 and len(scores) > 190221 + 10:
        print("Part 1: {}".format("".join([str(n) for n in scores[190221:190231]])))
        if done_part2:
            break
        done_part1 = True
        
