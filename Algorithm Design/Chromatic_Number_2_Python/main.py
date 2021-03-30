import functions
from graph import *

INPUT_INDEX = 1

#read data from input file and assign the returned tuple to n and a
n, a = functions.read_data("data\\input"+str(INPUT_INDEX)+".in")
g  = Graph(n) 
g.graph = a

#start of the program
chromatic_number = 1
result_updater = g.final_coloring_function(chromatic_number)
if result_updater == False:
    while result_updater == False:
        chromatic_number += 1
        result_updater = g.final_coloring_function(chromatic_number)

#print the computed chromatic number to "data.out"
print(chromatic_number, file = open("data\\data.out", "w"))