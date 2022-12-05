import re

def read_input(infile, stacks):
    with open(infile, 'r') as f:
        _stacks, instructions = f.read().strip().split('\n\n')
    for level in reversed(_stacks.split('\n')[:-1]):
        for col in range(9): # 9 stacks of crates
            if level[col * 4 + 1] != ' ':
                stacks[col].append(level[col * 4 + 1])
    instructions = [re.findall(r'move (\d+) from (\d) to (\d)', x)[0] for x in instructions.split('\n')]
    return list(map(lambda x: (int(x[0]), int(x[1]) - 1, int(x[2]) - 1), instructions))

def move_crates_9000(stacks, instructions):
    for num, src, dst in instructions:
        for _ in range(int(num)):
            stacks[dst].append(stacks[src].pop())

def move_crates_9001(stacks, instructions):
    temp = list()
    for num, src, dst in instructions:
        for _ in range(int(num)):
            temp.append(stacks[src].pop())
        for _ in range(int(num)):
            stacks[dst].append(temp.pop())

def get_crate_tops(stacks):
    result = ""
    for sidx in range(9):
        result += stacks[sidx][-1]
    return result

if __name__ == "__main__":
    stacks = [ [] for _ in range(9)] # 9 stacks of crates
    instructions = read_input("input.txt", stacks)
    move_crates_9000(stacks, instructions)
    print(get_crate_tops(stacks))
    stacks = [ [] for _ in range(9)]
    instructions = read_input("input.txt", stacks)
    move_crates_9001(stacks, instructions)
    print(get_crate_tops(stacks))
