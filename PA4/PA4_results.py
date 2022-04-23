'''
TO DO: Fix an issue with numbers that arent composed of 3 or 5, e.g. make it pass testing for 8, 97, and 512 
'''

def make_postage(money):

    if money == 0:
        return 0
    else:
        stamp_three = 0
        stamp_five = 0
        if money % 3 == 0:
            stamp_three = int(money/3)
        elif money % 5 == 0:
            stamp_five = int(money/5)
        else:
            stamp_three = 1
            stamp_five = 1
        return (stamp_five, stamp_three)


from itertools import permutations as pm
def permutations(tuple_pairs):
    permutation_list = pm(tuple_pairs)
    permutation_sets = { x for x in permutation_list }
    return permutation_sets
        
        
def permutation(s) :
    from itertools import permutations
    return set(permutations(s))


if __name__=='__main__' :
    amount = input()
    print("change for ", amount, " : ", make_postage(int(amount)))
    print("permutations:  ", permutations((1, 2)))
