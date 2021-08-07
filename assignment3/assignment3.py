"""
Represents a single item within the linked list.
"""
from typing import Tuple

class Node:
    # Initialize dictionary
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextNode = None
        
    def getKey(self):
        return self.key

    def getValue(self):
        return self.value
        
    def setNext(self, key, value):
        self.nextNode = Node(key, value)

    def get(self, key):
        if(self.key==None):
            raise RuntimeError("Node is empty")
        if(self.key!=key):
            raise RuntimeError("Key is invalid")                
        return self.value

    def delete(self, key):
        if(self.key==None):
            raise RuntimeError("Node is empty")
        if(self.key!=key):
            raise RuntimeError("Key is invalid")                
        return self.value == None

    def __iter__(self): #Should iterats over the Nodes in the list
        yield Tuple(self.key, self.value)
    
    def __str__(self):
        return str(self.key) + ":" + str(self.value)


"""
Collection of key-value pair records, implemented as a linked list.
"""
# Name of class MUST be Dictionary
class Dictionary:
    
      
    # Dictionary methodes start here:
    def __init__(self):
        self.__head = None

    """
    Save key-value pair record. Returns 'True' if inserted and 'False' if key is already in the Dictionary
    """
    def insert(self, key, value):
        if(self.__head == None):
            self.__head = Node(key, value)
            return True

        if(self.__head.key == key):
            return False
            
        nodeHolder = self.__head.nextNode
        while(nodeHolder is not None):
            if(nodeHolder.key == key):
                return False
            nodeHolder = nodeHolder.nextNode

        nodeHolder = self.__head
        while(nodeHolder is not None):
            if(nodeHolder.nextNode == None):
                nodeHolder.nextNode = Node(key, value)
                return True
            nodeHolder = nodeHolder.nextNode

    """
    Returns value that is identified by `key`, or None if no such key exists.
    """
    def get(self, key):
        if(self.__head == None):
            return RuntimeError("there is no such a key in the dic")

        if (self.__head.key == key):
            return self.__head.value

        nodeHolder = self.__head.nextNode
        while(nodeHolder is not None):
            if(nodeHolder.key == key):
                return nodeHolder.value 
            nodeHolder = nodeHolder.nextNode

        return RuntimeError("there is no such a key in the dic")


    """
    Delete key-value pair identified by `key` and returns 'True' if deleted, 'False' if not found in the Dictionary.
    """
    def delete(self, key):
        pass   # Abstract method, add your own
    
    """
        Returns a gererator that could iterate over the tupel (key, value) objects (orderd by key, smallest to largest)
    """
    def __iter__(self):
        pass   # Abstract method, add your own
    
    
    """ Returns a string representation of the key, values in the linked list from the start to the end (sorted).
    """
    def __str__(self):
        pass   # Abstract method, add your own

    def printMe(self):
        nodeHolder = self.__head
        while(nodeHolder is not None):
            print(nodeHolder)
            nodeHolder = nodeHolder.nextNode



d1 = Dictionary()
d1.insert("k1", "v1")
d1.insert("k1", "v1")
d1.insert("k2", "v2")
d1.insert("k3", "v3")

d1.printMe()

print(d1.get("k1"))
print(d1.get("k4"))
print(d1.get("k2"))

