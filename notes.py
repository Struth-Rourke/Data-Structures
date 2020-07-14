""" Monday """

command = input 

# if command in ["n", "s", "e", "w"]:

commands = ["n", "s", "e", "w", "q", "r"]


## Runtime Complexity

''' Constant Time Operation(s): '''
## An operation that takes the same amount of time regardless of input size -- Big O Notation: O(constant)
# (ex: list indexing, fetching from a dictionary via key)
commands[1] # Constant Time Operation

## (ex: fetching from a dictionary via key)
rooms = {"outside": Room(...), ...}
rooms["outside"] # Constant Time Operation



''' Linear Time Operations '''
## An operation that does depends on the size of the onput; the time operation 
## increases linearly with input size -- Big O Notation: O(n)
# (ex. For Loops)
for command in commands: # Linear Time Operation
    # TODO
    # Adding 1 to the list size, increases the number of loop iterations by c 
    # for some constant

for key, value in rooms.items(): # Linear Time Operation



''' Quadratic Time Operations '''
## An operation that does depends on the size of the onput; the time operation 
## increases quadratically with input size -- Big O Notation: O(m * n)

# (ex. print out every combination of pairs of commands from our command list)
for x in commands: # 6 Commands
    for y in commands: # 6 Commands
        print(x, y) # 36 Combinations
        # (n,n), (n,s), ...
        # (s,n), (s,s), ...
        # (e,n), (e,s), ...


''' Linked Lists '''
# Compare and contrast lists vs. arrays
# [1,2,3,4,5,6,7,...N] -- *contiguous