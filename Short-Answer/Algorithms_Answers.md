#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
The while loop is n^3 and the next line is n^2, making the overall complexity O(n). As n increase an additional operation will need to occur.


b) O(n log n)
 The for loop is linear and the while loop is log(n) since j is increased double instead of



c) O(n)
The recursive function calls itself one less time each time its called. The runtime increases as input increases

## Exercise II

Binary Search

find_floor(building):

    # Return the building floor if list is equal to 1
    # This will be the floor that eggs start breaking on
    if len(building) <= 2 and drop_egg(building[0]) == "doesnt break":
        return building[1]
    else:
        return building[0]

    # Create midpoint in the building
    midpoint = len(building)//2

    # If egg breaks, then recursively call the function with the left half of building data
    if drop_egg(building[midpoint]) == "break":
        return find_floor(building[:midpoint])

    # If egg desnt break, recursively call the function with the right half of building data
    elif drop_egg(building[midpoint]) == "doesnt break":
        return find_floor(building[midpoint:])


