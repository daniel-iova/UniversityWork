import functions
import input_handling

INPUT_INDEX = 1

#read input and store it into following variables
n, G, vertex_order, result, color = input_handling.read_data("data\\input"+str(INPUT_INDEX)+".in")

#assign colors to all vertices
for i in vertex_order:
    if result[i] == -1:
        color, result = functions.assign_color(G, vertex_order, n, i, color, result)

#assign the chromatic number
chromatic_number = max(result)+1

#print chromatic number to file "data.out"
print(chromatic_number, file = open("data\\data.out", "w"))
