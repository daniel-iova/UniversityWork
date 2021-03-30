class Graph(): 
    def __init__(self, no_nodes): 
        self.N = no_nodes 
        self.graph = [[0 for i in range(no_nodes)] for j in range(no_nodes)] 
  
    #checks if it safe to color "node" with color "c"
    def safe_to_color(self, node, coloring_result, c): 
        for i in range(self.N): 
            if self.graph[node][i] == 1 and coloring_result[i] == c: 
                return False
        return True
    
    #utility function used to clean up the final coloring function
    def graph_color_utility_function(self, m, coloring_result, node): 
        if node == self.N: 
            return True
  
        for c in range(1, m+1): 
            if self.safe_to_color(node, coloring_result, c) == True: 
                coloring_result[node] = c 
                if self.graph_color_utility_function(m, coloring_result, node+1) == True: 
                    return True
                coloring_result[node] = 0
        return False

    #final coloring function, returns true if the coloring is complete
    def final_coloring_function(self, m): 
        coloring_result = [0] * self.N 
        if self.graph_color_utility_function(m, coloring_result, 0) == False:
            return False
        
        return True
