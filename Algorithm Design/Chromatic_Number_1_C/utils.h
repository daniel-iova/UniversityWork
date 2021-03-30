/**
 * This function is used to check if the node
 * has any nodes connected to it of the same color
 * @param node - int
 * @param color - int
 */
void check_connected_same_color(int node, int color);

/**
 * This function is used to assign a color
 * to the current node
 * @param node - int
 * @param vertex_order - int[]
 */
void assign_color(int node, int vertex_order[]);

/**
 * Reads data from the given file
 * and stores it into the global variables
 * @param file - const char*
 */
void read_data(const char* file);

/**
 * Prints the resulting chromatic number
 * into the specified file
 * @param file - const char*
 */
void print_result(const char* file);
