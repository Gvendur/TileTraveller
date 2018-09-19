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

def direction_validation_check(user_input):
    if(direction in valid_direction and direction not in "()"):
        return True
    else:
        return False

def longitude_check(user_input):
    if user_input in longitude:
        return True
    elif user_input in latitude:
        return False

def new_valid_directions(x_axis, y_axis):
    if(y_axis == 1):
        return "(N)orth"
    elif(x_axis == 1 and y_axis == 2):
        return "(N)orth or (E)ast or (S)outh"
    elif(x_axis != 1 and (x_axis == y_axis)):
        return "(S)outh or (W)est"
    elif(x_axis == 3 and y_axis == 2):
        return "(N)orth or (S)outh"
    elif(x_axis == 1 and y_axis ==3):
        return "(E)ast or (S)outh"
    elif(x_axis == 2 and y_axis == 3):
        return "(E)ast or (W)est"


while True:
    print("You can travel: {0}.".format(valid_direction))
    while True:
        direction = input("Direction: ").upper()
        valid = direction_validation_check(direction)
        if valid:
            break
        elif not valid:
            print("Not a valid direction!")
        
    if longitude_check(direction):
        if(direction == "N"):
            position_y_axis += 1
        else:
            position_y_axis -= 1
    elif not longitude_check(direction):
        if(direction == "E"):
            position_x_axis += 1
        else:
            position_x_axis -= 1

    valid_direction = new_valid_directions(position_x_axis, position_y_axis)

    if(position_x_axis == 3 and position_y_axis == 1):
        break

print("Victory!")