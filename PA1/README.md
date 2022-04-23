In this assignment you will program a few functions that allow a list to have the functionality of a set data structure (remember list can have duplicates but sets do not so your code should not return duplicate values even if the input list contain duplicates). This includes creating a new set, adding/removing elements etc. Complete details are provided in the code template below. We have also (mostly) implemented two of the functions to give you an idea of what's expected (set_new(), and set_remove()). All the functions should be just a few lines of code.

In this assignment we will represent sets using the Python list data structure. For example:

s = [1,'a',3]

represents the mathematical set object {1, 'a', 3}.

Note that since order does not matter, the same set can be represented by a list that has the elements of the set in a different order. In your implementation, the result returned by your code should not depend on the order in which the elements appear in the list.

Your job is to implement the following set operations:
