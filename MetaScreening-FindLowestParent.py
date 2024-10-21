
# what kind of tree? Binary Tree
# define N: number of nodes in the tree

# if tree is balanced, L, which is layer in tree would be Log(N)
# Space O(L) = O(LOG(N))
# Time O(L) = O(LOG(N))

# if tree is not balanced, L, which is layer in tree would be equal to N
# Space O(L) = O(N)
# Time O(L) = O(N)

ListNode:
- node key
- node.parent
- node.children

def findLowestCommonAncestor(n1, n2):

    n2Chain = set()
    def buildChain(node):
        if node:
            n2Chain.add(node)
            buildChain(node.parent)
    buildChain(n2)

    def searchChain(node, targetChain):
        if node:
            if node in targetChain:
                return node
            searchChain(node.parent)
    return searchChain(n1, n2Chain)


# Variation where we use the children information: we keep track of the 2 nodes' depth, prop the lower one up one step at a time, until they are equal, then that should be the lowest common node
def findLowestCommonAncestor(n1, n2):

    def propNodeUp(node): # return parent node 1 level up
        return node.parent

    def dfs(node, D):


    n1Depth = dfs(n1, 0)
    n2Depth = dfs(n2, 0)

    while True:
        if n1Depth == n2Depth and n1 == n2:
            return n1
        elif n1Depth < n2Depth:
            n2 = propNodeUp(n2)
            n2Depth -= 1
        else:
            n1 = propNodeUp(n1)
            n1Depth -= 1
