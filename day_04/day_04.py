def read_input(infile):
    with open(infile, 'r') as f:
        _input = [[list(map(int, y.split('-'))) for y in x.strip().split(',')] for x in f.readlines()]
    return _input

def check_contained(pair):
    for _pair in pair, list(reversed(pair)):
        if _pair[0][0] >= _pair[1][0] and _pair[0][1] <= _pair[1][1]:
            return True
    return False

def count_contained(pairs):
    count = 0
    for pair in pairs:
        count += 1 if check_contained(pair) else 0
    return count

if __name__ == "__main__":
    assignment_pairs = read_input("input.txt")
    print(count_contained(assignment_pairs))
