#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "graph.h"
#include "functions.h"

#define INPUT_INDEX 1

int main(void) {
    struct Graph graph;

    /// build and read the input from the given file and assign it to the graph object
    char input_str[] = "data\\input";
    char index[3];
    itoa(INPUT_INDEX, index, 10);
    strcat(input_str, index);
    strcat(input_str, ".in");
    read_data(&graph, (const char*)input_str);

    /// initialize the chromatic number and the coloring result array
    int chromatic_number = 1;
    int coloring_result[graph.n];
    /// use result_updater to see if the coloring_result is correct
    int result_updater = final_coloring_function(graph, chromatic_number, coloring_result);

    /// increment the chromatic number until every spot inside the coloring function is filled
    if (!result_updater)
        while (!result_updater){
            chromatic_number++;
            result_updater = final_coloring_function(graph, chromatic_number, coloring_result);
        }

    /// print the chromatic number to a file "data.out"

    FILE *outfile = fopen("data\\data.out", "w");
    fprintf(outfile, "%d", chromatic_number);

    fclose(outfile);
    free(graph.graph);
    return 0;
}
