# Tile Traveller algorithm description: 
# Before the game begins:
#      We will think of the game as a coordinate grid with x and y axis.
#      We define two variables: position_x_axis and postion_y_axis and give them the value 1. 
#      That will be the starting position.
#      Next we will define two variables called longitude and latitude.
#      longtitude will have the value "NS" and latitude "WE"
#      Then we will define the valid_direction = "(N)orth" this will be the only valid position
#      from the starting position.
#
# Step 1: The program will print the valid directions.
# Step 2: Program will ask for a direction
# Step 3: Program will check if the user input is a valid direction: if the input is valid the program 
#         will continue to step 4 otherwise step 3 will be repeated.
# Step 4: When the user inputs a valid direction the program will check if it is a longitude or latitude
# Step 5: If it is a longitude then one will be added to position_y_axis if the direction is north and one will be subtracted
#         from position_y_axis if it is south
#         If it is a latitude then one will be added to position_x_axis if the direction is east and one will 
#         be subtracted from position_x_axis if it is west. 
# Step 6: If the position_x_axis has the value 1 and position_y_axis has the value 3 the program will go to step 8.
#         If not the program will go to step 7.
# Step 7: The program will determine the valid directions from the position on the grid and go to step 1.
# Step 8: The program will print out "Victory !" and end.

position_x_axis = 1
position_y_axis = 1

longitude = "NS"
latitude = "WE"

valid_direction = "(N)orth"