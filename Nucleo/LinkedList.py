# -*- coding: utf-8 -*-

class Node:
    
    def __init__(self, value):
        
        self.value = value 
        self.next = None

class LinkedList:

    def __init__(self):
        self.first = None
    
    def push(self, value, position = 0):
        
        if(not isinstance(position,int) or position<0):
            return False

        if(not self.first):
            self.first = Node(value)
            return True
        
        count = 0

        """
        current = self.first

        if(count == position):
        
            self.first = Node(value)
            self.first.next = current
            return True
        """

        before = self.first
        current = self.first.next
    
        while(before):

            count += 1
            if(count == self.length()):

                before.next = Node(value)    
                before.next.next = current
                return True

            before = before.next
            current = current.next
            
        current = Node(value)
        return True
    
    def print(self):

        current = self.first
        string = ""

        while(current):

            string += (("%s => ")%(current.value))
            current = current.next
        
        string += "null"
        print(string)
    
    def delete(self, position):

        count = 1 
        before = self.first
        current = self.first.next

        if(position == 0):
            
            after = self.first.next.next
            self.first = Node(self.first.next.value)
            self.first.next = after
            return True
        
        while(current):

            if(count == position):

                before.next = before.next.next
                return True
            
            count += 1
            before = before.next
            current = current.next
    
    def search(self, value):

        current = self.first
        count = 0

        while(current):

            if(current.value == value):
                print("El valor %s se encuentra en la posicion %s" %(value, count))

            count += 1
            current = current.next
    
    def length(self):
    
        current = self.first
        count = 0

        while(current):

            count += 1
            current = current.next
            
        return count