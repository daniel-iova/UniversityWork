#include "graph.h"

int safe_to_color(struct Graph g, int vertex, int coloring_result[], int color) {
    for (int i = 0; i < g.n; i++) {
        if (g.graph[vertex][i] == 1 && coloring_result[i] == color) {
            return 0;
        }
    }
    return 1;
}

int graph_color_utility_function(struct Graph g, int chromatic_number, int coloring_result[], int vertex) {
    if (vertex == g.n) {
        return 1;
    }
    for (int c = 1; c <= chromatic_number; c++) {
        if (safe_to_color(g, vertex, coloring_result, c)) {
            coloring_result[vertex] = c;
            if (graph_color_utility_function(g, chromatic_number, coloring_result, vertex + 1)) {
                return 1;
            }
            coloring_result[vertex] = 0;
        }
    }
    return 0;
}

int final_coloring_function(struct Graph g, int chromatic_number, int coloring_result[]) {
    for (int i = 0; i < g.n; i++) {
        coloring_result[i] = 0;
    }
    if (!graph_color_utility_function(g, chromatic_number, coloring_result, 0))
        return 0;
    return 1;
}

