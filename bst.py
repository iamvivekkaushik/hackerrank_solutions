def calculateFact(fact: list, N: int) -> None:
 
    fact[0] = 1
    for i in range(1, N):
        fact[i] = fact[i - 1] * i
 
# Function to get the value of nCr
def nCr(fact: list, N: int, R: int) -> int:
 
    if (R > N):
        return 0
 
    # nCr= fact(n)/(fact(r)*fact(n-r))
    res = fact[N] // fact[R]
    res //= fact[N - R]
 
    return res
 
# Function to count the number of ways
# to rearrange the array to obtain same BST
def countWays(arr: list, fact: list) -> int:
 
    # Store the size of the array
    N = len(arr)
 
    # Base case
    if (N <= 2):
        return 1
 
    # Store the elements of the
    # left subtree of BST
    leftSubTree = []
 
    # Store the elements of the
    # right subtree of BST
    rightSubTree = []
 
    # Store the root node
    root = arr[0]
 
    for i in range(1, N):
 
        # Push all the elements
        # of the left subtree
        if (arr[i] < root):
            leftSubTree.append(arr[i])
 
        # Push all the elements
        # of the right subtree
        else:
            rightSubTree.append(arr[i])
 
    # Store the size of leftSubTree
    N1 = len(leftSubTree)
 
    # Store the size of rightSubTree
    N2 = len(rightSubTree)
 
    # Recurrence relation
    countLeft = countWays(leftSubTree, fact)
    countRight = countWays(rightSubTree, fact)
 
    return (nCr(fact, N - 1, N1) *
            countLeft * countRight)
 
# Driver Code
if __name__ == '__main__':
 
    arr = [ 3, 4, 5, 1, 2 ]
 
    # Store the size of arr
    N = len(arr)
 
    # Store the factorial up to N
    fact = [0] * N
 
    # Precompute the factorial up to N
    calculateFact(fact, N)
     
    print(countWays(arr, fact))
