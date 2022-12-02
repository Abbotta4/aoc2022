def read_input(infile):
    with open(infile, 'r') as f:
        _input = [x.strip().split(' ') for x in f.readlines()]
    return _input

def do_round(round):
    them, me = ord(round[0]) - 64, ord(round[1]) - 87
    if me % 3 == them - 1:
        return me
    elif me == them:
        return me + 3
    else:
        return me + 6
    

def calculate_score(rounds):
    score = 0
    for round in rounds:
        score += do_round(round)
    return score

if __name__ == "__main__":
    rounds = read_input("input.txt")
    print(calculate_score(rounds))
