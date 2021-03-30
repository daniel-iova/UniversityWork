#include <stdio.h>
#include <stdlib.h>
#include "graph.h"

void read_data(struct Graph* g, const char* file) {
    int x, y;
    g->edges = 0;
    FILE* f = fopen(file, "r");
    fscanf(f, "%d", &(g->n));
    g->graph = (int **)malloc(g->n * sizeof(int *));
    for (int i = 0; i < g->n; i++){
        g->graph[i] = (int *)malloc(g->n * sizeof(int));
    }
    for (int i = 0; i < g->n; i++)
        for (int j = 0; j < g->n; j++)
            g->graph[i][j] = 0;
    while (fscanf(f, "%d %d", &x, &y) != EOF) {
        g->graph[x][y] = 1;
        g->graph[y][x] = 1;
        g->edges++;
    }
    fclose(f);
}
