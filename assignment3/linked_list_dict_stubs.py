"""
Collection of key-value pair records, implemented as a linked list.
"""
# Name of class MUST be Dictionary
class Dictionary:
    
    """
    Represents a single item within the linked list.
    """
    class Node:
        # Initialize dictionary
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.nextNode = None
            
        def getKey(self):
            
            pass   # Abstract method, add your own

        def getValue(self):

            pass   # Abstract method, add your own
            
        def insert(self, key, value):
            
            pass   # Abstract method, add your own

        def get(self, key):

            pass   # Abstract method, add your own

        def delete(self, key):

            pass   # Abstract method, add your own
        
        def __iter__(self): #Should iterats over the Nodes in the list
            
            pass   # Abstract method, add your own
        
        def __str__(self):

            pass   # Abstract method, add your own
        
    # Dictionary methodes start here:
    def __init__(self):
        self.__head = None

    """
    Save key-value pair record. Returns 'True' if inserted and 'False' if key is already in the Dictionary
    """
    def insert(self, key, value):
        pass   # Abstract method, add your own

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