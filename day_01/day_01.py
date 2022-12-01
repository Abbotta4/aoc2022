def read_input(infile):
    with open(infile, 'r') as f:
        _input = [[int(y) for y in x.splitlines()] for x in f.read().split('\n\n')]
    return _input

def find_most_calories(elves):
    return sum(sorted(elves, key=lambda elf: sum(elf))[-1])

if __name__ == "__main__":
    elves = read_input("input.txt")
    print(find_most_calories(elves))
