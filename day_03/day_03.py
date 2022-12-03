from more_itertools import chunked

def read_input(infile):
    with open(infile, 'r') as f:
        _input = [[x[:len(x)//2], x[len(x)//2:].strip()] for x in f.readlines()]
    return _input

def find_common_item(rucksack):
    for item in rucksack[0]:
        if item in rucksack[1]:
            return item

def get_priority(item):
    return ord(item) - 96 if item.islower() else ord(item) - 38

def find_priority_sum(rucksacks):
    sum = 0
    for ruck in rucksacks:
        sum += get_priority(find_common_item(ruck))
    return sum

def find_badge(group):
    for item in group[0]:
        if item in group[1]:
            if item in group[2]:
                return item

def find_badge_sum(rucksacks):
    sum = 0
    for group in chunked([''.join(x) for x in rucksacks], 3):
        sum += get_priority(find_badge(group))
    return sum

if __name__ == "__main__":
    rucksacks = read_input("input.txt")
    print(find_priority_sum(rucksacks))
    print(find_badge_sum(rucksacks))
