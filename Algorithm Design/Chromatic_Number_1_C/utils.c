#include <stdio.h>
#include <stdlib.h>
#include "global_variable.h"

int check_connected_same_color(int node, int color){

    for (int i = 0; i < no_nodes; i++){
        if (G[node][i] == 1 && color == result[i]){
            return 1;
        }
    }
    return 0;
}

void assign_color(int node, int vertex_order[])
{
    int ok = 0;
    for (int i = 0; i < no_nodes; i++){
        if (G[node][vertex_order[i]] == 0 && result[vertex_order[i]] == -1 && !check_connected_same_color(vertex_order[i], color)){
            ok = 1;
            result[vertex_order[i]] = color;
        }
    }
    if (ok)
        color++;
}

void read_data(const char* file){
    int x, y;
    FILE *f = fopen(file, "r");
    fscanf(f, "%d", &no_nodes);
    G = (int **)malloc(no_nodes * sizeof(int *));
    for (int i = 0; i < no_nodes; i++){
        G[i] = (int *)malloc(no_nodes * sizeof(int));
    }
    for(int i = 0; i < no_nodes; i++)
        for(int j = 0; j < no_nodes; j++)
            G[i][j]=0;
    while (fscanf(f, "%d %d", &x, &y) != EOF){
        G[x][y]=1;
        G[y][x]=1;
    }
    result = (int *)malloc(no_nodes * sizeof(int));
    for (int i = 0; i < no_nodes; i++){
        result[i] = -1;
    }
    fclose(f);
}

void print_result(const char* file){

    FILE *g = fopen(file, "w");
    int chrn = 0;
    for(int i = 0; i < no_nodes; i++){
        if (result[i] > chrn)
            chrn = result[i];
    }
    fprintf(g, "%d\n", chrn+1);
    fclose(g);
}
