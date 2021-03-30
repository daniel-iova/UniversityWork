#read data from given file and return tuple of n and g
def read_data(file):
    with open(file) as f:
        n = int(next(f).split()[0])
        g = [[0 for i in range(n)] for j in range(n)]
        for line in f:
            x, y = line.split()
            x = int(x)
            y = int(y)
            g[x][y] = 1
            g[y][x] = 1
    return n, g