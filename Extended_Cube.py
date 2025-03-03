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

import random  # for scrambles, etc

import itertools  #  for iterating through lists



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



def check(left_array, front_array, right_array, top_array, bottom_array, back_array):

##    left_array = [0,0,0,0]
##    front_array = [1,1,1,1]
##    right_array = [2,2,2,2]
##    top_array = [3,3,3,3]
##    bottom_array = [4,4,4,4]
##    back_array = [5,5,5,5]

    for num in left_array:
        if (num != 0):
            break
        for num in front_array:
            if (num != 1):
                break
            for num in right_array:
                if (num != 2):
                    break
                for num in top_array:
                    if (num != 3):
                        break
                    for num in bottom_array:
                        if (num != 4):
                            break
                        for num in back_array:
                            if (num != 5):
                                break
                            print("You Win")
                            return 1
                            model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
                            exit()
def solve(left_array,front_array, right_array, top_array, bottom_array, back_array):
    rd = copy.deepcopy(right_array)
    fd = copy.deepcopy(front_array)
    botd = copy.deepcopy(bottom_array)
    backd = copy.deepcopy(back_array)
    ld = copy.deepcopy(left_array)
    td = copy.deepcopy(top_array)
    seed_list = [1,2,3,4,5,6,7,8,9,10,11,12]  #List of all possible moves
    perm_list = [perm_list]  #List of lists, this is algorithmically added on to to make the list longer every time this program runs
                            #Every sub list is iterated through and modeled then checked against solve
    input("Press Enter To begin solving.  Warning this is intensive process!  Will solve in 11 moves or less")
    solved = check(left_array, front_array, right_array, top_array, bottom_array, back_array)
    #perm_list.append = 
    while (solved != 1):
        turn_seed = random.randint(1,12)
        turns = 11
        while(turns != 0):
            solved = check(ld,fd,rd,td,botd,backd)
            if (solved == 1):
                print("Finished")
                break
            #strategy 1 is to make stacks of all combos and try them all
            #strategy 2 is to make list of lists using seed_list and perm_list
        
        solved = check(left_array, front_array, right_array, top_array, bottom_array, back_array)





        
def rand_solve(left_array,front_array, right_array, top_array, bottom_array, back_array):
    #Highly inefficient solver, will not work
    input("Press Enter To begin solving.  Warning this is anintensive process and will likely never resolve before heat death of universe")
    solved = check(left_array, front_array, right_array, top_array, bottom_array, back_array)
    while (solved != 1):
        
        seed = random.randint(1,12)
        if (seed == 1):
            right_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)

        if (seed == 2):
            left_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 3):
            back_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 4):
            bottom_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 5):
            front_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 6):
            top_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 7):
            right_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)

        if (seed == 8):
            left_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 9):
            back_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 10):
            bottom_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 11):
            front_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 12):
            top_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)

        solved = check(left_array, front_array, right_array, top_array, bottom_array, back_array)
def input_handler(left_array, front_array, right_array, top_array, bottom_array, back_array,gameyn):  #This function handles all inputs to the program from the command line
    #handle user input
    model_cube(left_array, front_array, right_array, top_array, bottom_array, back_array)
    user_in = 'h'
    while (user_in != "q"):
        user_in = input("turn the cube (h for help, q to quit): ")

        if(gameyn == 1):
            check(left_array, front_array, right_array, top_array, bottom_array, back_array)
                
        if(user_in == 'h'):
            print("r = right clockwise; l = left clockwise; t = top clockwise; f = front clockwise; u = bottom clockwise; b = bottomclockwise");
            print("\nplace a c after corresponding face letter demarcation to make a counter-clockwise turn")
            print("\nType test to run a pre written test program, you may change the test in this file yourself")
            print("\nType steptest to step through tests individually, for debug, may not be implemented yet")
            print("\nType g for game mode, g-w to write scramble to file, g-l to load Scramble from file")
            print("\nType g-r to random solve, this will likely go on for eternity")
            print("\nType g-s to intelligently solve in 11 moves or less")
        
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
        if(user_in == 'test' or user_in == 'steptest'):
            if(user_in == 'step_test'):
                exit() #not yet implemented
                tester(left_array, front_array, right_array, top_array, bottom_array, back_array, 1)
            tester(left_array, front_array, right_array, top_array, bottom_array, back_array, 0)
        if(user_in == 'q'):
            exit()

def array_setup():#left_array, front_array, right_array, top_array, bottom_array, back_array):
    #Sets up the array
##    left_array = [0,1,2,3]    #Old array method, * use this method to ensure that methods work so you can see scramble
##    front_array = [4,5,6,7]
##    right_array = [8,9,10,11]
##    top_array = [12,13,14,15]
##    bottom_array = [16,17,18,19]
##    back_array = [20,21,22,23]

    #New array numbering method, *ONLY USE WHEN METHODS CERTIFIED CORRECT*
    left_array = [0,0,0,0]
    front_array = [1,1,1,1]
    right_array = [2,2,2,2]
    top_array = [3,3,3,3]
    bottom_array = [4,4,4,4]
    back_array = [5,5,5,5]
    
    return left_array, front_array, right_array, top_array, bottom_array, back_array
def tester(left_array, front_array, right_array, top_array, bottom_array, back_array,stepyn):
    #This program sets up a test case to make sure that the program works
    left_array, front_array, right_array, top_array, bottom_array, back_array = array_setup()
    print("Right Turn")
    right_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Right Counter")
    right_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Back Turn")
    back_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Back Counter")
    back_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Bottom Turn")
    bottom_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Bottom Counter")
    bottom_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Top Turn")
    top_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Top Counter")
    top_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Left Turn")
    left_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Left Counter")
    left_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Front Turn")
    front_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Front Counter")
    front_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
    print("Finished")
   
    exit()





def scramble(left_array, front_array, right_array, top_array, bottom_array, back_array, writeyn):
#Still need to implement code to stop unscrambling while scrambling, ie right to right counter right after
    #num_scram = random.randint(6,45)
    num_scram = 45 # For Testing if check works, REWRITE TO DO MINIMUM NUM SCRAMBLES AND CHECK FOR UNSCRAMBLING 
    for i in range(num_scram):
        seed = random.randint(1,12)
        if (seed == 1):
            right_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)

        if (seed == 2):
            left_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 3):
            back_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 4):
            bottom_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 5):
            front_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 6):
            top_turn(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 7):
            right_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)

        if (seed == 8):
            left_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 9):
            back_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 10):
            bottom_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 11):
            front_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)
            
        if (seed == 12):
            top_counter(left_array, front_array, right_array, top_array, bottom_array, back_array)

def main():
    #init arrays and go to main loop
    front_array = []
    back_array = []
    left_array = []
    right_array = []
    bottom_array = []
    top_array = []
    left_array, front_array, right_array, top_array, bottom_array, back_array = array_setup()
    user_in = input("g)ame (-w to write to game)(-l to load scramble file),(-s to solve with brute force), m)odel,: ")
    if (user_in == 'g'):
        scramble(left_array, front_array, right_array, top_array, bottom_array, back_array, 0)
        input_handler(left_array, front_array, right_array, top_array, bottom_array, back_array,1)
       # game()# rewrite input handler to do this with gameyn signature
    if (user_in == 'g-w'):
        scramble(left_array, front_array, right_array, top_array, bottom_array, back_array, 0)
        input_handler(left_array, front_array, right_array, top_array, bottom_array, back_array,1)
    
    if(user_in == 'g-r'):
        scramble(left_array, front_array, right_array, top_array, bottom_array, back_array, 0)
        rand_solve(left_array, front_array, right_array, top_array, bottom_array,back_array)
    if(user_in == 'g-s'):
        scramble(left_array, front_array, right_array, top_array, bottom_array, back_array, 0)
        solve(left_array, front_array, right_array, top_array, bottom_array,back_array)
    if (user_in == 'g-l'):
        load_scramble()
        input_handler(left_array, front_array, right_array, top_array, bottom_array, back_array,0)
    
    if (user_in == 'm'):
        left_array, front_array, right_array, top_array, bottom_array, back_array = array_setup()
        input_handler(left_array, front_array, right_array, top_array, bottom_array, back_array,0)
    
    #input_handler(left_array, front_array, right_array, top_array, bottom_array, back_array,0)
    
main() 
    
