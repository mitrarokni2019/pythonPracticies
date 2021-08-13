## Dictionary ADT ##
## Implemented with BS Tree
"""
Collection of key-value pair records, implemented as a binary search tree.
"""
# Name of class MUST be Dictionary



from Assignment3LinkedList import Node


class Dictionary:
    class Node:
        def __init__(self, key, value):
            self.key    = key
            self.value  = value
            self.left   = None
            self.right  = None

        def getKey(self):
            return self.key   # Abstract method, add your own

        def getValue(self):
            return self.value   # Abstract method, add your own
            
        def insert(self, key, value):
            pass  # Abstract method, add your own

        def get(self, key):
            if(self.key==None):
                print("Node is empty")
            if(self.key!=key):
                print("Key is invalid")                
            return self.value   # Abstract method, add your own

        def delete(self, key):
            if(self.key==None):
                print("Node is empty")
            if(self.key!=key):
                print("Key is invalid")                
            return self.value == None   # Abstract method, add your own
        
        def __iter__(self): #Should iterats over the Nodes in the tree
           # yield Tuple(self.key, self.value)   # Abstract method, add your own
            pass
        def __str__(self):
            return str(self.key) + ":" + str(self.value)   # Abstract method, add your own
        
        # def __delete(self, key):
            
        #     if(self.key==None):
        #         print("Node is empty")
        #     if(self.key!=key):
        #         print("Key is invalid")                
        #     else:
        #         return self == None  # Help method for delete (optional)
               
        def __getSmallest(self):
            current_node = self
                
            while current_node.left_child:
                current_node = current_node.left_child
            return current_node
        
# Dictionary methods start here:
    def __init__(self):
        self.__tree = None
        self.root = None

    """
    Save key-value pair record. Returns 'True' if inserted and 'False' if key is already in the Dictionary
    """
    def _insert (self,temp, key,value):
    
        if  key < temp.key:
            if temp.left == None:
                temp.left = self.Node(key,value)
                return True
            else:
                self._insert(temp.left,key, value)
            
        elif key > temp.key:
            if temp.right == None:
                temp.right = self.Node(key,value)
                
            else:
                self._insert(temp.right ,key, value)


          
    def insert(self,  key, value):
        if self.root == None:
            self.root = self.Node(key,value)
            return True
        else:
            self._insert(self.root, key, value)

    """
    Returns value that is identified by `key`, or None if no such key exists.
    """
    def _get(self,temp, key):
        if key == temp.key:
            return temp.value

        if  key < temp.key:

            if temp.left == None:
                print("the node is empty ")
                
            elif temp.left.key == key:
                return temp.left.value
                
            else:
                return self._get(temp.left,key)
            
        elif key > temp.key:
            if temp.right == None:
                print("thenode is empty ")

            elif temp.right.key == key:
                return temp.right.value
            
            else:
                return self._get(temp.right ,key)
    
    def get(self, key):
        if self.root == None:
            print(" Dic is empty there is no value to return ")
        else:
            return self._get(self.root, key)
        
        # Abstract method, add your own

    """
    Delete key-value pair identified by `key` and returns 'True' if deleted, 'False' if not found in the Dictionary.
    """
    def _delete(self, temp,  key):
        
        if key < temp.key:
            temp =  _delete(temp.left, key)
            

        elif key > temp.key:
            temp = _delete(temp.right, key)
            

        elif key == temp.key:
            if temp.right is None:
                temp =  temp.left
                return temp

            elif temp.left is None:
                temp = temp.right
                return temp

            else: 
                temp= __getSmallest(self)           
                 
        else:
            print("there is no such akey in dic!")     # Abstract method, add your own

        def delete(self, key):
            if self.root == None:
             print(" Dic is empty there is no value to be deleted ")
            else:
                return self._delete(self.root, key)
            
    
    """
        Returns a gererator that could iterate over the tupel (key, value) objects (orderd by key, smallest to largest)
    """
    def __iter__(self):
        return iter(self.dictionary)   # Abstract method, add your own
    
    """ Returns a string representation of the key, values in the tree in order after key value (smallest to largest)
    """
    def __str__(self):
        return str(self)   # Abstract method, add your own
    
        """     def printMe(self):
        nodeHolder = self.root
        while(nodeHolder is not None):
            print(nodeHolder)
            nodeHolder = nodeHolder.right """


ww = Dictionary()
ww.insert("k5", "5")
ww.insert("k2", "2")
ww.insert("k1", "1")
ww.insert("k0", "0")
ww.insert("k3", "3")
ww.insert("k5", "5")
ww.insert("k7", "7")
ww.get("k3")
print(ww.get("k3"))
print(ww.get("k7"))




""" ww.printMe() """
