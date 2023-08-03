class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def validatebst(root):
    return helper(root, float('-inf'), float('inf'))

def helper(root, low, high):
    if root is None:
        return True
    if root.val <= low or root.val >= high:
        return False
    return helper(root.left, low, root.val) and helper(root.right, root.val, high)

#Time Complexity is O(n) as we have to traverse through all the nodes
#Space Complecity is O(n) as we need to store the entire tree while recursion

n1 = TreeNode(45)
n2 = TreeNode(35)
n3 = TreeNode(68)
n4 = TreeNode(15)
n5 = TreeNode(42)
n6 = TreeNode(64)
n7 = TreeNode(78)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

print(validatebst(n1))