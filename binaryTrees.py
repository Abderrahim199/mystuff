import time
# i will try to make binary trees myself!!!

class binaryTree():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def insert(root,node):
    if root is None:
        root = node
    else:
        if node.data > root.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                    
                insert(root.left, node)

def isbinary(root):
    if root is None:
        return True
    elif root.right is not None and root.right.data < root.data:
        return False
    elif root.left is not None and root.left.data > root.data:
        return False
    else:
        return isbinary(root.left) or isbinary(root.right)

def inorder(root):
    if root is None:
        return []
    else:
        return inorder(root.left) + [root.data] + inorder(root.right)


def maxTree(root):
    listo = inorder(root)
    if listo is []:
        return None
    else:
        max = listo[0]
        for element in listo:
            if element > max:
                max = element
    return max


def minTree(root):
    listo = inorder(root)
    
    if listo is []:
        return None
    else:
        min = listo[0]
        for element in listo:
            if element < min:
                min = element
    return min


then = time.time()


Tree = binaryTree(2)
listo = [3,6,2,3,9,6,1]
for element in listo:
    insert(Tree,binaryTree(element))


print(isbinary(Tree))
print(maxTree(Tree))
print(minTree(Tree))
print(inorder(Tree))
# the end



print('time taken is : %s in ms' % (round((time.time() - then)*1000, 4)))



