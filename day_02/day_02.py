def read_input(infile):
    with open(infile, 'r') as f:
        _input = [x.strip().split(' ') for x in f.readlines()]
    return _input

def do_p1_round(round):
    them, me = ord(round[0]) - 64, ord(round[1]) - 87
    if me % 3 == them - 1:
        return me
    elif me == them:
        return me + 3
    else:
        return me + 6

def do_p2_round(round):
    them, outcome = ord(round[0]) - 64, (ord(round[1]) - 88) * 3
    if outcome == 0:
        return outcome + (them - 1) if them - 1 > 0 else 3
    elif outcome == 3:
        return outcome + them
    else:
        return outcome + them % 3 + 1

def calculate_score(rounds, part):
    score = 0
    for round in rounds:
        if part == 1:
            score += do_p1_round(round)
        else:
            score += do_p2_round(round)
    return score

if __name__ == "__main__":
    rounds = read_input("input.txt")
    print(calculate_score(rounds, 1))
    print(calculate_score(rounds, 2))
