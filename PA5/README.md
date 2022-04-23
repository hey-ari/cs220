This fourth python programming assignment, PA4, is about combinations. You will write a function comb(A,n,k,p,lo) that prints all k out of n combinations of 0…n-1 in lexicographical order. The parameters p and lo represent the current location to be filled (p) and the first number to pick in that location (lo). The array A is used to create and store the current combination. The algorithm for enumerating combinations is discussed in lecture 17 Permutations.

   python3 comb.py 5 3
   
produces

  [0, 1, 2]
  [0, 1, 3]
  [0, 1, 4]
  [0, 2, 3]
  [0, 2, 4]
  [0, 3, 4]
  [1, 2, 3]
  [1, 2, 4]
  [1, 3, 4]
  [2, 3, 4]
