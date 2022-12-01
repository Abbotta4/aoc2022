def read_input(infile):
    with open(infile, 'r') as f:
        _input = [[int(y) for y in x.splitlines()] for x in f.read().split('\n\n')]
    return _input

def find_most_calories(elves):
    return sum(sorted(elves, key=lambda elf: sum(elf))[-1])

def find_top_three(elves):
    return sum([sum(x) for x in sorted(elves, key=lambda elf: sum(elf))[-3:]])

if __name__ == "__main__":
    elves = read_input("input.txt")
    print(find_most_calories(elves))
    print(find_top_three(elves))
