class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        #Checking if root node is empty or not
        if root is None:
            return -1
        count = 1
        #calculating height of left subtree
        left_subtree_height = self.getHeight(root.left)
        #calculating height of right subtree
        right_subtree_height = self.getHeight(root.right)
        #if l_sb is greater than r_sb then initial count is added to the total height
        if left_subtree_height > right_subtree_height:
            return count + left_subtree_height
        else:
            return count + right_subtree_height

T=3
arr=[3, 5, 2]
myTree=Solution()
root=None
for i in range(T):
    for data in arr:
        #data=int(input())
        root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)