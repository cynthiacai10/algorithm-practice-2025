# Binary Search Tree implementation
# Author: Cynthia
# Date: August 17, 2025

# BST properties:
# - The left subtree of a node contains only values less than the node’s value.
# - The right subtree of a node contains only values greater than the node’s value.

# BST traversals:
# - Inorder: left subtree -> root -> right subtree
# - Preorder: root -> left subtree -> right subtree
# - Postorder: left subtree -> right subtree -> root

from collections import deque

class TreeNode:
    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left = left_node
        self.right = right_node


class BinarySearchTree:
    def __init__(self):
        # Initialize an empty BST
        self.root = None

    def insert(self, val: int) -> bool:
        # Insert val into BST, return True if inserted, False if duplicate
        if self.isEmpty():
            self.root = TreeNode(val)
            return True
        
        curr = self.root
        while curr:
            if curr.val > val: # in left subtree
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    return True
            elif curr.val < val: # in right subtree
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    return True
            else: # duplicate
                return False
        
    def search(self, val: int) -> bool:
        # Search for val in BST, return True if found else False
        curr = self.root
        while curr:
            if curr.val > val: # in left subtree
                curr = curr.left
            elif curr.val < val: # in right subtree
                curr = curr.right
            else:
                return True
        return False

    def delete(self, val: int) -> bool:
        # TO-DO!
        # Delete val from BST, return True if deleted else False
        if self.isEmpty():
            return False

        curr = self.root
        while curr:
            if curr.val > val: # in left subtree
                if curr.left:
                    curr = curr.left
                else:
                    return False
            elif curr.val < val: # in right subtree
                if curr.right:
                    curr = curr.right
                else:
                    return False
            else: # find it, delete

                return True

    def getMin(self) -> int:
        # Return the minimum value in BST, or -1 if empty
        if self.isEmpty():
            return -1
        
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        # Return the maximum value in BST, or -1 if empty
        if self.isEmpty():
            return -1
        
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def isEmpty(self) -> bool:
        # Return True if the tree is empty, otherwise False
        return False if self.root else True

    def inorder(self) -> list:
        # Return inorder traversal (sorted order) as a list
        # left -> root -> right
        if self.isEmpty():
            return []
        

    def preorder(self) -> list:
        # Return preorder traversal as a list
        # root -> left -> right
        if self.isEmpty():
            return []
        
        preorder = []
        q = deque([self.root])
        while q:
            for node in q:
                preorder.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return preorder

    def postorder(self) -> list:
        # Return postorder traversal as a list
        # left -> right -> root
        pass


def test_bst():
    bst = BinarySearchTree()

    # Test 1: Insert elements
    assert bst.insert(10) == True     # insert root
    assert bst.insert(5) == True      # insert left child
    assert bst.insert(15) == True     # insert right child
    assert bst.insert(3) == True      # insert left-left
    assert bst.insert(7) == True      # insert left-right
    assert bst.insert(12) == True     # insert right-left
    assert bst.insert(18) == True     # insert right-right
    assert bst.insert(10) == False    # duplicate insert should fail

    # Test 2: Search
    assert bst.search(7) == True
    assert bst.search(12) == True
    assert bst.search(100) == False   # not in tree

    # Test 3: Traversals
    assert bst.inorder() == [3, 5, 7, 10, 12, 15, 18]
    assert bst.preorder() == [10, 5, 3, 7, 15, 12, 18]
    assert bst.postorder() == [3, 7, 5, 12, 18, 15, 10]

    # Test 4: Get Min/Max
    assert bst.getMin() == 3
    assert bst.getMax() == 18

    # Test 5: Delete leaf node
    assert bst.delete(3) == True
    assert bst.inorder() == [5, 7, 10, 12, 15, 18]

    # Test 6: Delete node with one child
    assert bst.delete(5) == True
    assert bst.inorder() == [7, 10, 12, 15, 18]

    # Test 7: Delete node with two children
    assert bst.delete(15) == True
    assert bst.inorder() == [7, 10, 12, 18]

    # Test 8: Delete non-existing element
    assert bst.delete(100) == False

    # Test 9: Final Min/Max after deletions
    assert bst.getMin() == 7
    assert bst.getMax() == 18

    print("✅ All test cases passed!")


if __name__ == "__main__":
    # Run tests
    test_bst()
