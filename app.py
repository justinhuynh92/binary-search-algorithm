# a function that takes a list and target parameter
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        #show the start and end of the list
        print('Step', steps, ":" , str(list[start:end+1]))

# multiple variables : middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position
