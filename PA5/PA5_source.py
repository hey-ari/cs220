import sys

def comb(A,n,k,p,lo):
  """
    n>=1, k<=n, p: position to fill, lo: first number to pick
    print all possible subsets of k out of n
  """

if __name__ == "__main__":
  d = len(sys.argv)>3
  n = int(sys.argv[1])
  k = int(sys.argv[2])
  A = []
  for i in range(k):
      A.append(0)
  if d: print("n:",n,"k:",k)
  comb(A,n,k,0,0)
  
