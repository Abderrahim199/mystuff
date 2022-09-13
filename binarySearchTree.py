
def insert(node, key , value):
    if node is None:
        node = binaryTree(key,value)
    elif  key < node.key:
        node.left = insert(node.left, key , value)
        node.left.parent = node
    elif  key >= node.key:

        node.right = insert(node.right, key, value)    
        node.right.parent = node
    return node
def find(node, key):
    if node is None:
        return None
    elif key == node.key:
        return (node.key,(node.value.email,node.value.name))
    elif key > node.key:
        return find(node.right, key)
    else:
        return find(node.left, key)

    # we are done!!!!

def update(node,key, value):
    target = find(node,key)
    if target is not None:
        target.value = value

def balanced(root):
    
    if root is None:
        return True, 0
    balanced_l,height_l = balanced(root.left)
    balanced_r,height_r = balanced(root.right)
    isbalanced = balanced_l and balanced_r and abs(height_r - height_l) <= 1
    hight = 1 + max(height_l,height_r)
    return isbalanced,hight

def make_balanced_tree(data, lo = 0 , hi = None, parent = None):
    if hi is None:
        hi = len(data)-1
    if lo > hi:
        return None
    mid = (lo + hi)//2
    key,value = data[mid]
    root = binaryTree(key,value)
    root.parent = parent
    root.left = make_balanced_tree(data,lo,mid-1,root)
    root.right = make_balanced_tree(data,mid+1,hi,root)
    return root

def inorder(root):
    if root is None:
   j     return []
    else:
        return inorder(root.left) + [(root.key,root.value)] + inorder(root.right)
def balance_bst(node):
    return make_balanced_tree(inorder(node))

def sizeTree(root):
    return len(inorder(root))
def display(root,space = '\t', level=0):

    if root is None:
        print(space*level + '@')
        return
    
    if root.left is None and root.right is None:
        print(space*level + str(root.key))
        return 

    display(root.right, space, level +1)
    print(space*level + str(root.key))
    display(root.left,space, level + 1)

# let's code the Treee!!!
class User():
    def __init__(self,name,username,email):
        self.name = name
        self.username = username
        self.email = email
        def __repr__(self):
            return "User(name = {} , username = {} , email = {} ".format(self.name,self.username,self.email)
        def __str__(self):
            return self.__repr__()

class binaryTree():
    def __init__(self,key,value=None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.parent = None





class treemap():
    def __init__(self):
        self.root = None
        
    def __setitem__(self, key, value):
        node = find(self.root,key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key , value)

    def __getitem__(self,key):
        node = find(self.root,key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in inorder(self.root))

    def __len__(self):
        return sizeTree(self.root)
    def display(self):
        return display(self.root)

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')

jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')


sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')


users = [aakash,hemanth,jadhesh,siddhant,sonaksh,vishal]


print('here is our testing for the code')

treemap1 = treemap()



treemap1['biraj'] = biraj
treemap1['hemanth'] = hemanth
treemap1['siddhant'] = siddhant
treemap1['vishal'] = vishal

print(treemap1.display())


for key,value in treemap1:
    print(key,value.email)



















