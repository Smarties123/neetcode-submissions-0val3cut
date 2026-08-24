
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                minNode = root.right

                while minNode.left:
                    minNode = minNode.left
                
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return root