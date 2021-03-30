struct Graph {
    int n;
    int **graph;
    int edges;
};

/**
 * This function is used to check if it is safe
 * to color the current vertex
 * @param g - struct Graph
 * @param vertex - int
 * @param coloring_result - int[]
 * @param color - int
 */
int safe_to_color(struct Graph g, int vertex, int coloring_result[], int color);

/**
 * This is a utility function used
 * to build the coloring_result array
 * @param g - struct Graph
 * @param chromatic_number - int
 * @param coloring_result - int[]
 * @param vertex - int
 */
int graph_color_utility_function(struct Graph g, int chromatic_number, int coloring_result[], int vertex);

/**
 * This is the final coloring function in which the coloring result
 * is built by calling the graph_color_utility_function
 * @param g - struct Graph
 * @param chromatic_number - int
 * @param coloring_result - int[]
 */
int final_coloring_function(struct Graph g, int chromatic_number, int coloring_result[]);
