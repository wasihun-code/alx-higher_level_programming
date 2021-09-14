#!/usr/bin/python3
# same directory.
import swaps

# Import x and y variables using 
# file_name.variable_name notation
new_x = swaps.x
new_y = swaps.y
print("x value: ", new_x, "y value:", new_y)
# Similarly, import swapVal method from swaps file
x , y = swaps.swapVal(new_x,new_y)

print("x value: ", x, "y value:", y)
