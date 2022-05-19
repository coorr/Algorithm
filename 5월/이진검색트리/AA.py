from asyncio.windows_events import NULL
import sys
from turtle import left
sys.stdin=open("5월/이진검색트리/input.txt","r")

class Node:
    def __init__(self, data):
        self.data =data
        self.left = None
        self.right= None
        
class BinarySearchTree:
    def __init__(self,root):
        self.root = root
        print(self.root)
    def insert(self, data):
        print("data = " , data)
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                print("node.left = ",node.left)
                node.left = self._insert_value(node.left, data)
            else:
                print("node.right = ",node.right)
                node.right = self._insert_value(node.right, data)
        return node
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        print("root = ", root)
        
        print("key = ", key)
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
                

root = Node(1)
bst = BinarySearchTree(root)
bst.insert(2)
bst.insert(7)
bst.insert(8)
bst.insert(NULL)
print(bst.find(2))
print(bst.find(12))
                
        
        
        
    
    

        



    
    
    
    


