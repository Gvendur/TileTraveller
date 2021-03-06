# Tile Traveller algorithm description: 
# Before the game begins:
#      We will think of the game as a coordinate grid with x and y axis.
#      We define two variables: position_x_axis and postion_y_axis and give them the value 1. 
#      That will be the starting position.
#      Next we will define two variables called longitude and latitude.
#      Longitude will have the value "NS" and latitude "WE"
#      Then we will define the valid_direction and set it to "(N)orth". This will be the only valid position
#      from the starting position.
#
# Step 1: The program will print the valid directions.
# Step 2: Program will ask for a direction
# Step 3: Program will check if the user input is a valid direction: if the input is valid the program 
#         will continue to step 4 otherwise step 3 will be repeated.
# Step 4: The program will check if the user input is a longitude or a latitude
# Step 5: If it is a longitude then one will be added to position_y_axis if the direction is north and one will be subtracted
#         from position_y_axis if it is south
#         If it is a latitude then one will be added to position_x_axis if the direction is east and one will 
#         be subtracted from position_x_axis if it is west. 
# Step 6: If the position_x_axis has the value 1 and position_y_axis has the value 3 the program will go to step 8.
#         If not the program will continue to step 7.
# Step 7: The program will determine the valid directions from the new position on the grid and go to step 1.
# Step 8: The program will print out "Victory !" and end.

position_x_axis = 1
position_y_axis = 1

longitude = "NS"
latitude = "WE"

valid_direction = "(N)orth"

while True:
    print("You can travel: {0}.".format(valid_direction))
    while True:
        direction = input("Direction: ").upper()
        if(direction in valid_direction and direction not in "()"):
            break
        else:
            print("Not a valid direction!")
        
    if(direction in longitude):
        if(direction == "N"):
            position_y_axis += 1
        else:
            position_y_axis -= 1
    elif(direction in latitude):
        if(direction == "E"):
            position_x_axis += 1
        else:
            position_x_axis -= 1

    if(position_x_axis == 3 and position_y_axis == 1):
        break

    if(position_y_axis == 1):
        valid_direction = "(N)orth"
    elif(position_x_axis == 1 and position_y_axis == 2):
        valid_direction = "(N)orth or (E)ast or (S)outh"
    elif(position_x_axis != 1 and (position_x_axis == position_y_axis)):
        valid_direction = "(S)outh or (W)est"
    elif(position_x_axis == 3 and position_y_axis == 2):
        valid_direction = "(N)orth or (S)outh"
    elif(position_x_axis == 1 and position_y_axis ==3):
        valid_direction = "(E)ast or (S)outh"
    elif(position_x_axis == 2 and position_y_axis == 3):
        valid_direction = "(E)ast or (W)est"

print("Victory!")