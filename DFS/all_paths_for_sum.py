# https://www.educative.io/courses/grokking-the-coding-interview/B815A0y2Ajn
# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# helper method
def find_paths(root, sum):
    allPaths = []
    find_paths_recursive(root, sum, [], allPaths)
    return allPaths

def find_paths_recursive(currentNode, sum, currentPath, allPaths):
    # we've gone off the deep end
    if currentNode is None:
        return

    # add currentNode to our path
    currentPath.append(currentNode)

    # if we are at a leaf and the path value is 0, we have a valid path
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))

    # check the left subtree and right subtree 
    find_paths_recursive(currentNode.left, sum - currentNode.val, currentPath, allPaths)
    find_paths_recursive(currentNode.right, sum - currentNode.val, currentPath, allPaths)

    # backtrack up a node. 
    currentPath.pop()

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
