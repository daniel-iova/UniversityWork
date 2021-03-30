#include <stdio.h>
#include <stdlib.h>
#include "generate_array.h"
#include "global_variable.h"

int degree_of_node(int node){
    int degree = 0;
    for (int i = 0; i < no_nodes; i++){
        if (G[node][i])
            degree++;
    }
    return degree;
}

int cmp(const void *a, const void *b) {
    const int *ia = (const int *)a;
    const int *ib = (const int *)b;
    int diff = degree_of_node(*ib)  - degree_of_node(*ia);
    if (diff == 0){
        return *ia - *ib;
    }
    return diff;
}

void generate_list_by_degree(int vertex_order[], int no_nodes){
    for (int i = 0; i < no_nodes; i++){
        vertex_order[i] = i;
    }
    qsort(vertex_order, no_nodes, sizeof(int), cmp);
}
