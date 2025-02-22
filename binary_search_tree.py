#binary tree

class Treenode:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
    #      1
    #     2    3
    #   4   5   10 

A = Treenode(1)
B = Treenode(2)
C = Treenode(3)
D = Treenode(4)
E = Treenode(5)
F = Treenode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)

#Recursive post-order Traversal
def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)