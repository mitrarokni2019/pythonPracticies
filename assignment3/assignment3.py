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
        return set(self.key) + ":" + set(self.value)


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

    """
    Returns value that is identified by `key`, or None if no such key exists.
    """
    def get(self, key):
        pass   # Abstract method, add your own

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