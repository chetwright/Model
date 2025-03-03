#This is a Python language refactoring by Chet Wright of a non-working C program written by the same author for
#CSC 372 Survery of Artificial Intelligence as taught by Dr. Thomas Allen at Centre College in Danville, Kentucky
#which seeks to provide the user with the ability to model a working 2x2 Rubiks cube in text format which they may manipulate
#via various commands
#Written by Chet Wright

#         | 12  13|
#             Top
#         | 14  15|

#   0   1 | 4   5 | 8   9  | 20  21 
#    Left   Front    Right    Back
#   2   3 | 6   7 | 10  11 | 22  23

#         | 16  17|
#           Under(Bottom)   
#         | 18  19|
#
#       As opposed to cells which are the numbered 0,1,2,3 in each array and have a color marker as the program
#       was originally designed with this way allows the program to be color agnostic for any cube and for solving
#       I believe a simple check for all positions in each array being numerically sequential will suffice
#       ie: for cells in right_array:
#               if (right_array[0] == right_array[1] - 1) && (right
#                   etc... for all 3 cells and for all 6 arrays
#                   This should work but may need to be reordered in one way or another as the cells can indeed
#                   be out of order in value but still be color matched, the advantage is that each cubit is modeled in this way
#                   Either need to use tuple packing or duplicate arrays(what was done here) for this to work properly
#                   To check use all commands and then reverse them to see if the arrays return to their previous state
#                   If this works on all then the program should be in working order
import copy # Need to avoid shallow copying the lists, serious problem if you shallow copy the lists

def right_turn(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)
    
    right_array[0] = rd[2]
    right_array[1] = rd[0]
    right_array[2] = rd[3]
    right_array[3] = rd[1]
    
    front_array[1] = botd[1]
    front_array[3] = botd[3]
 
    
    top_array[1] = fd[1]
    top_array[3] = fd[3]

    
    bottom_array[1] = backd[0] #Remember backside flips around
    bottom_array[3] = backd[2]


   
    back_array[0] = td[1]
    back_array[2] = td[3]
    

    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array
    
    
def right_counter(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)

    right_array[0] = rd[1]
    right_array[1] = rd[3]
    right_array[2] = rd[0]
    right_array[3] = rd[2]

    front_array[1] = td[1]
    front_array[3] = td[3]
    
    top_array[1] = backd[0]
    top_array[3] = backd[2]

    bottom_array[1] = fd[1]
    bottom_array[3] = fd[3]

    back_array[0] = botd[1]
    back_array[2] = botd[3]
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array
def left_turn(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)
    
    left_array[0] = ld[2]
    left_array[1] = ld[0]
    left_array[2] = ld[3]
    left_array[3] = ld[1]

    front_array[0] = td[0]
    front_array[2] = td[2]

    back_array[1] = botd[2]
    back_array[3] = botd[0]

    bottom_array[0] = fd[0]
    bottom_array[2] = fd[2]

    top_array[0] = backd[3]
    top_array[2] = backd[1]
    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array

def left_counter(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)  
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)

    left_array[0] = ld[1]
    left_array[1] = ld[3]
    left_array[2] = ld[0]
    left_array[3] = ld[2]

    front_array[0] = botd[0]
    front_array[2] = botd[2]
    
    top_array[0] = fd[0]
    top_array[2] = fd[2]

    back_array[1] = td[2]
    back_array[3] = td[0]

    bottom_array[0] = backd[3]
    bottom_array[2] = backd[1]
    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array

def front_turn(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)

    front_array[0] = fd[2]
    front_array[1] = fd[0]
    front_array[2] = fd[3]
    front_array[3] = fd[1]

    top_array[3] = ld[1]
    top_array[2] = ld[3]

    left_array[1] = botd[0]
    left_array[3] = botd[1]

    right_array[0] = td[2]
    right_array[2] = td[3]

    bottom_array[0] = rd[2]
    bottom_array[1] = rd[0]
    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array

def front_counter(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)
    
    front_array[0] = fd[1]
    front_array[1] = fd[3]
    front_array[2] = fd[0]
    front_array[3] = fd[2]

    top_array[2] = rd[0]
    top_array[3] = rd[2]

    left_array[1] = td[3]
    left_array[3] = td[2]

    right_array[0] = botd[1]
    right_array[2] = botd[0]

    bottom_array[0] = ld[1]
    bottom_array[1] = ld[3]
    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array

def top_turn(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)
    
    top_array[0] = td[2]
    top_array[1] = td[0]
    top_array[2] = td[3]
    top_array[3] = td[1]

    left_array[0] = fd[0]
    left_array[1] = fd[1]

    back_array[0] = ld[0] #Check back later
    back_array[1] = ld[1]

    right_array[0] = backd[0]
    right_array[1] = backd[1]

    front_array[0] = rd[0]
    front_array[1] = rd[1]
    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array

def top_counter(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)

    top_array[0] = td[1]
    top_array[1] = td[3]
    top_array[2] = td[0]
    top_array[3] = td[2]

    left_array[0] = backd[0]
    left_array[1] = backd[1]

    back_array[0] = rd[0]
    back_array[1] = rd[1]

    right_array[0] = fd[0]
    right_array[1] = fd[1]

    front_array[0] = ld[0]
    front_array[1] = ld[1]
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array

def bottom_turn(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)

    bottom_array[0] = botd[2]  #due to the curve in, or as I call it, 'the flip', this becomes much harder to conceptualize I find
    bottom_array[1] = botd[0]
    bottom_array[2] = botd[3]
    bottom_array[3] = botd[1]

    front_array[2] = rd[2]
    front_array[3] = rd[3]

    right_array[2] = backd[2]
    right_array[3] = backd[3]

    back_array[2] = ld[2] 
    back_array[3] = ld[3]

    left_array[2] = fd[2]
    left_array[3] = fd[3]
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array
def bottom_counter(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)
    bottom_array[0] = botd[1]  
    bottom_array[1] = botd[3]
    bottom_array[2] = botd[0]
    bottom_array[3] = botd[2]

    front_array[2] = ld[2]
    front_array[3] = ld[3]

    back_array[3] = rd[3]
    back_array[2] = rd[2]

    left_array[2] = backd[2]
    left_array[3] = backd[3]

    right_array[2] = fd[2]
    right_array[3] = fd[3]
    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array
def back_turn(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)

    back_array[0] = backd[2]
    back_array[1] = backd[0]
    back_array[2] = backd[3]
    back_array[3] = backd[1]
    
    right_array[1] = td[0]
    right_array[3] = td[1]

    left_array[0] = botd[2]
    left_array[2] = botd[3]

    top_array[0] = ld[2]
    top_array[1] = ld[0]

    bottom_array[2] = rd[3]
    bottom_array[3] = rd[1]

    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array

def back_counter(left_array, front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)

    back_array[0] = backd[1]
    back_array[1] = backd[3]
    back_array[2] = backd[0]
    back_array[3] = backd[2]
    
    right_array[1] = botd[3]
    right_array[3] = botd[2]

    left_array[0] = td[1]
    left_array[2] = td[0]
    
    top_array[0] = rd[1]
    top_array[1] = rd[3]

    bottom_array[2] = ld[0]
    bottom_array[3] = ld[2]
    
    
    
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    return left_array, front_array, right_array, top_array, bottom_array, back_array

def model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array):
    #Models the cubes current state
    long_space = "          "
    short_space = "   "
    med_space = "        "
    print("",long_space,long_space,top_array[0],short_space,top_array[1],"\n",long_space,long_space,"Top\n\n",long_space,long_space,top_array[2],short_space,top_array[3],"\n")
    print("\n",left_array[0],short_space,left_array[1],long_space,front_array[0],short_space,front_array[1],long_space,right_array[0],short_space,right_array[1],long_space,back_array[0],short_space,back_array[1])
    print("\n","Left",long_space,"Front",long_space,"Right",long_space,"Back")
    print("\n",left_array[2],short_space,left_array[3],long_space,front_array[2],short_space,front_array[3],long_space,right_array[2],short_space,right_array[3],med_space,back_array[2],short_space,back_array[3])
    print("\n",long_space,long_space,bottom_array[0],short_space,bottom_array[1])
    print("\n",long_space,long_space,"Bottom")
    print("\n",long_space,long_space,bottom_array[2],short_space,bottom_array[3])
    
def input_handler(left_array, front_array, right_array, top_array, bottom_array, back_array):  #This function handles all inputs to the program from the command line
    #handle user input
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    user_in = 'h'
    while (user_in != "q"):
        user_in = input("turn the cube (h for help, q to quit): ")
                
        if(user_in == 'h'):
            print("r = right clockwise; l = left clockwise; t = top clockwise; f = front clockwise; u = bottom clockwise; b = bottomclockwise");
            print("\nplace a c after corresponding face letter demarcation to make a counter-clockwise turn")
        if(user_in == 'r'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = right_turn(left_array, front_array, right_array, top_array, bottom_array, back_array);
            
        if(user_in == 'rc'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = right_counter(left_array, front_array, right_array, top_array, bottom_array, back_array);
            
        if(user_in == 'l'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = left_turn(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'lc'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = left_counter(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'f'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = front_turn(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'fc'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = front_counter(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 't'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = top_turn(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'tc'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = top_counter(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'u'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = bottom_turn(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'uc'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = bottom_counter(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'b'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = back_turn(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'bc'):
            left_array, front_array, right_array, top_array, bottom_array, back_array = back_counter(left_array, front_array, right_array, top_array, bottom_array, back_array);
        if(user_in == 'q'):
            exit()
def array_setup():#left_array, front_array, right_array, top_array, bottom_array, back_array):
    #Sets up the array
    left_array = [0,1,2,3]
    front_array = [4,5,6,7]
    right_array = [8,9,10,11]
    top_array = [12,13,14,15]
    bottom_array = [16,17,18,19]
    back_array = [20,21,22,23]
    return left_array, front_array, right_array, top_array, bottom_array, back_array
def main():
    #init arrays and go to main loop
    front_array = []
    back_array = []
    left_array = []
    right_array = []
    bottom_array = []
    top_array = []
    left_array, front_array, right_array, top_array, bottom_array, back_array = array_setup()
    input_handler(left_array, front_array, right_array, top_array, bottom_array, back_array)

main()
    
