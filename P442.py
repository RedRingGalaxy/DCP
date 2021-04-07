# Problem Statement [Hard]
'''
A cartesian tree with sequence S is a binary tree defined by the following two properties:
1. Its Heap ordered, so that each parent value stricktly less than of its children
2. An In-order traversal fo the tree producess nodes with values that correspond exactly to S.

ex: S = [3, 2 , 6, 1, 9]
  1 
 / \
 2  9
/ \
3   6

'''
# TODO: Tree Node base class
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = self.right = None

# TODO: Insert the given value seems like min heap and return Node       
def Insert(root,value) -> Node:

    if root.value > value:
        temp = Node(value)
        temp.left = root
        root = temp
    elif root.value < value and root.right != None:
        root.right = Insert(root.right , value)
    else:
        temp = Node(value)
        root.right = temp

    return root

# TODO: Pop the value of parent node and return poped value and new tree
def Pop(root) -> tuple:
    if root == None:
        return 0

    left = root.left
    right = root.right
    rslt = root.value

    root = MergeTree(left,right)

    return (rslt, root)

# TODO: Merge and return two trees into one
def MergeTree(left, right) -> Node:
    root = None
    if left == None:
        return right

    if right == None:
        return left

    if left.value < right.value and left.right != None:
        left.right = MergeTree(left.right, right)
        root = left
    elif left.value < right.value and left.right == None: 
        left.right = right
        root = left
    elif left.value > right.value and right.left != None:
        right.left = MergeTree(right.left, left)
        root = right
    elif left.value > right.value and right.left != None:
        right.left = left
        root = right

    return root

# TODO: To convert the cartesian tree into a array
def TreeToSeq(root) -> list:
    if root == None:
        return []

    lst = TreeToSeq(root.left)
    lst.append(root.value)
    lst += TreeToSeq(root.right)

    return lst

# TODO : Build cartesian tree from given array
def SeqToTree(seqList) -> Node:
    
    if len(seqList) < 1:
        return

    root = None
    temp = None

    for i in range(len(seqList)):
        if i == 0:
            root = Node(seqList[i])
        else:
            root = Insert(root, seqList[i])
        
    return root

# TODO: Method to print Tree
def PrintTree(root,pos = "root -> ") -> None:
    
    if root == None:
        return

    PrintTree(root.left , pos + " left -> ")
    print(pos , root.value)
    PrintTree(root.right,  pos + " right -> ")

# TODO: Main method
if __name__ == "__main__":
    root = SeqToTree([3, 2, 6, 10, 5, 12])
    lst = TreeToSeq(root)
    print(lst)
    val, root =  Pop(root)
    print(val)
    PrintTree(root)
    val, root =  Pop(root)
    print(val)
    PrintTree(root)
    val, root =  Pop(root)
    print(val)
    PrintTree(root)





