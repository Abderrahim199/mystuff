# here, i'm going to learn how to deal with linked lists!.
class Node():
    def __init__(self,a_number):
        self.data = a_number
        
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None


    def append(self, value):
        if self.head  is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def showElements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        

    def length(self):
        
        length = 0
        current = self.head
        while current is not None:
            length +=1
            current = current.next
        return length



    def get_element(self,position):
        
        pos = 0
        
        current = self.head
        while pos<position and current.next is not None:
            pos +=1
            current = current.next
        return current.data


    def reverse(self):
        if self.head is None:
            return None
        
        prev = None
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        
        return prev.data


def reverse(l):
    if l.head is None:
        return None
    current = l.head
    prev = None
    while current:
        empt = current
        current = current.next
        empt.next = prev
        prev = empt
    l.head = prev


            





list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)

print('the lenght of our linkedlist is :' ,list2.length())
print('the number in the position 2 : ', list2.get_element(2))




print('this is the head: ', list2.reverse())










    
