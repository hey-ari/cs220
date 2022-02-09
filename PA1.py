def set_new():
    """Return a new set"""
    return []


def set_remove(s, value):
    """Remove the given value from the set s"""
    # perform some type checking to see that the user
    # has provided the right kind of input:
    if type(s) != type([]):
        raise ValueError
    # we can simply use the "remove" method of a list:
    s.remove(value)

    # create an empty list to keep unrepeated values
    duplicatesRemoved = set_new()
    # go through values using a loop
    for item in s:
    # add items that aren't in new list already
        if item not in duplicatesRemoved:
            duplicatesRemoved.append(item)
    # assign new values to s
    s = duplicatesRemoved
    return s


def set_union(s1, s2):
    """Return the union of sets s1 and s2 as a list"""
    if type(s1) != type([]) or type(s2) != type([]):
        raise ValueError
    # add new empty list
    outcome = set_new()

    #remove any duplicates in union of s1 and s2
    # go through 1st list and add to outcome if not there already.
    for item in s1:
        if item not in outcome:
            outcome.append(item)

    # same for 2nd list
    for item in s2:
        if item not in outcome:
            outcome.append(item)

    return outcome


def set_intersection(s1, s2):
    """Return the intersection of sets s1 and s2 as a list"""
    if type(s1) != type([]) or type(s2) != type([]):
        raise ValueError

    outcome = set_new()

    # go through  items in 1st list and if item is in 2nd list add it to outcome
    for item in s1:
        if item in s2 and item not in outcome:
            outcome.append(item)

    return outcome

def set_membership(s, value):
    """Return True if value is in the set s, and False otherwise"""
    if type(s) != type([]):
        raise ValueError
    # check if value in s and return a boolean value
    if value in s:
        return True
    else:
        return False


def set_equals(s1, s2):
    """Return True if the sets s1 and s2 have exactly the same elements"""
    if type(s1) != type([]) or type(s2) != type([]):
        raise ValueError

    # temporary list
    burner = set_new()

    # remove duplicates
    for item in s1:
        if item not in burner:
            burner.append(item)
    s1 = burner

    # same for s2
    burner = set_new()
    for item in s2:
        if item not in burner:
            burner.append(item)
    s2 = burner

    equal = True
    # if length isn't equal, returns False
    if len(s1) == len(s2):
        for item in s1:
            if item not in s2:
                equal = False
                break
    else:
        equal = False
    return equal

def set_difference(s1, s2):
    """Return the set difference of s1 and s2"""
    if type(s1) != type([]) or type(s2) != type([]):
        raise ValueError

    # empty list
    outcome = set_new()
    # go through s1, add if item not in s2 and outcome. duplicates are removed.
    for item in s1:
        if item not in s2 and item not in outcome:
            outcome.append(item)
    return outcome


def is_subset(s1, s2):
    """Return True if s1 is a subset of s2"""
    if type(s1) != type([]) or type(s2) != type([]):
        raise ValueError

    # go through s1. if item not in s2 then not a subset, break
    subset = True
    for item in s1:
        if item not in s2:
            subset = False
            break

    return subset


def is_proper_subset(s1, s2):
    """Return True if s1 is a proper subset of s2"""
    if type(s1) != type([]) or type(s2) != type([]):
        raise ValueError

    # same approach as is_subset.
    subset = True
    for item in s1:
        if item not in s2:
            subset = False
            break
    # check if proper subset
    proper = False
    # proceed if subset. go through s2. if item not in s1, found at least 1 item in s2 that is not in s1.
    # flag True and break.
    if subset:
        for item in s2:
            if item not in s1:
                proper = True
                break
    return proper




# set lists to test functions above
listA = []
listB = []
# print test results
print("Intersection in:", set_intersection(listA, listB))
print("Are equal: ", set_equals(listA,listB))
print("Deferences: ", set_difference(listA,listB))
print("Is Subset: ", is_subset(listA,listB))
print("Is Proper Subset: ", is_proper_subset(listA,listB))
