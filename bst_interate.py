# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest n umber
        """
        node = self.stack.pop()
        result = node.val
        if node.right != None:
            node = node.right
            while node != None:
                self.stack.append(node)
                node = node.left
        return result
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()