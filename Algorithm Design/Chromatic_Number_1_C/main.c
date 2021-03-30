#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "generate_array.h"
#include "utils.h"
#include "global_variable.h"

#define INPUT_INDEX 1

int main()
{

    /// build and read from given file and store data into global variables
    char input_str[] = "data\\input";
    char index[3];
    itoa(INPUT_INDEX, index, 10);
    strcat(input_str, index);
    strcat(input_str, ".in");
    read_data((const char*)input_str);

    /// generate array with indices sorted by highest degree first
    int vertex_order[no_nodes];
    generate_list_by_degree(vertex_order, no_nodes);

    /// assign colors to the vertices in sorted order
    for(int i = 0; i < no_nodes; i++){
        if (result[vertex_order[i]] == -1)
            assign_color(vertex_order[i], vertex_order);
    }

    /// print the chromatic number to the given file
    print_result("data\\data.out");
    /// free allocated memory
    free(G);
    free(result);
    return 0;
}
