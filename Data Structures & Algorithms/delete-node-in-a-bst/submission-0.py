class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            successor = root.right
            while successor.left is not None:
                successor = successor.left

            # Replace current value with successor's value
            root.val = successor.val

            # Delete the duplicate successor node
            root.right = self.deleteNode(root.right, successor.val)

        return root