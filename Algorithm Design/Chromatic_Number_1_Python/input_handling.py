import functions

#reads data from given file and returns a tuple comprised of:
# - number of nodes
# - adjacency matrix
# - array with vertices ordered by the highest degree
# - array to store the result in
# - initial color
def read_data(file):
    with open(file) as f:
        n = int(next(f).split()[0])
        G = functions.make_matrix(n)
        for line in f:
            x, y = line.split()
            x = int(x)
            y = int(y)
            G[x][y] = 1
            G[y][x] = 1
        vertex_order = functions.get_sorted_by_degree_array(G, n)
        color = 0
        result = [-1 for x in range(n)]
    return n, G, vertex_order, result, color