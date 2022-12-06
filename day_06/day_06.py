import itertools, collections

def read_input(infile):
    with open(infile, 'r') as f:
        signal = f.read().strip()
    return signal

# recipe from https://docs.python.org/3/library/itertools.html
def sliding_window(iterable, n):
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def get_packet_start(signal):
    for idx, char in enumerate(sliding_window(signal, 4)):
        if len(set(char)) == len(char):
            return idx + 4
    
if __name__ == "__main__":
    signal = read_input("input.txt")
    print(get_packet_start(signal))
