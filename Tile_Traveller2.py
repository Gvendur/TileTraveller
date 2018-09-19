# 1. Which implementation was easier and why?
#       Implementation number 2. With functions you are able to divide the problem into 
#       smaller steps and have a better structure instead of just one long block of code.
# 2. Which implementation is more readable and why?
#       Implementation number 2. When using functions you can divide the code into small sections
#       instead of just one block of code. The name of the functions are also very descriptive 
#       for what they do.
# 3. Which problems in the first implementations were you able to solve with the later
#    implementation?
#       The program still works the same. The only problem I had with the first implementation
#       was readability. With implementation number 2 it was easier to read and understand how it works.
#       When I ran into errors with implemenation number 2 they were much easier to fix then when 
#       I ran into errors while coding implementation number 1. 
#
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

def new_position(direction, position):
    if direction == "N" or direction == "E":
        position += 1
        return position
    if direction == "S" or direction == "W":
        position -= 1
        return position

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

def user_won(x_axis, y_axis):
    if(x_axis == 3 and y_axis == 1):
        return True
    return False

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
        position_y_axis = new_position(direction, position_y_axis)
    elif not longitude_check(direction):
        position_x_axis = new_position(direction, position_x_axis)

    valid_direction = new_valid_directions(position_x_axis, position_y_axis)

    if user_won(position_x_axis, position_y_axis):
        print("Victory!")
        break