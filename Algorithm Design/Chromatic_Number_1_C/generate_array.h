/**
 * Returns the number of nodes
 * the current node is connected to
 * @param node - int
 */
int degree_of_node(int node);

/**
 * Comparator function for qsort based on
 * the degrees of the nodes
 * @param a - const void*
 * @param b - const void*
 */
int cmp(const void *a, const void *b);

/**
 * Function returns an array with the node indices
 * ordered based on their degree
 * @param vertex_order - int[]
 * @param n - int
 */
void generate_list_by_degree(int vertex_order[], int no_nodes);
