## This code was written for one of the Reeborg's World challenges. In the game, I wrote a code to help Reeborg, lost in a dark maze, to find the exit. 
## Check the following website for the challenge:
## https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

## front_is_clear(), right_is_clear(), turn_left(), and move() functions are all built-in in the game. 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# to prevent going into an infinite loop when the reeborg's front is clear.
while front_is_clear(): 
    move()
turn_left()
       
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()
