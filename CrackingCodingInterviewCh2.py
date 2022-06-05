
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 2 - Linked List'''

# 2.1 - Remove Duplicates
# Write code to remove duplicates from an unsorted linked list. 
# FOLLOW-UP: How would you solve this problem if a temporary buffer is not allowed? 

def removeDups(node):
    # Use a set to track duplicates
    duplicates = {}

    #Traverse through the unsorted linked list, starting the head
    prev = None
    while (node != None):
        #If value is in the duplicates set, point previous node's next pointer to the current node's next pointer.
        if (node.value in duplicates):
            prev.next = node.next
        else:
            duplicates.add(node.value)
            prev = node

        #Advance to the next node
        node = node.next

'''Alternative Scenario - with no buffer'''
def removeDups(head):
    # Create a pointer that will traverse through entire linked list
    current = head

    while (current != None):
        #Create another node that checks all subsequent nodes for duplicates
        runner = current

        #Traverse the runner through the list, starting at the next node
        while (runner.next != None): 
            if (runner.next.value == current.value):
                runner.next = runner.next.next
            else: 
                runner = runner.next
        
        #Once runner traverses through entire list, move the current pointer
        current = current.next 




def main(): 
    pass

main() 
