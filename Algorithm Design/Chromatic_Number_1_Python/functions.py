#creates matrix
def make_matrix(n):
    g = [[0 for column in range(n)] for row in range(n)]
    return g

#returns an array sorted by degrees
def get_sorted_by_degree_array(g, n):
    a = [x for x in range(n)]
    a = sorted(a, reverse=True, key = lambda x: sum(g[x]))
    return a

#checks if the current node is connected to any nodes of current color
def check_connected_same_color(G, n, node, color, result):
    for i in range(n):
        if G[node][i] == 1 and color == result[i]:
            return True
    return False

#assign colors to the result array
def assign_color(G, vertex_order, n, node, color, result):
    ok = 0
    for i in range(n):
        if G[node][vertex_order[i]] == 0 and result[vertex_order[i]] == -1 and check_connected_same_color(G, n, vertex_order[i], color, result) == False:
            ok = 1
            result[vertex_order[i]] = color
    if ok == 1:
        color += 1
    return color, result
