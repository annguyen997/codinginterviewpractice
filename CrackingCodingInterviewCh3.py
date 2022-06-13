
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 3 - Stacks and Queues'''


# 3.1 - Three in One
# Describe how you could use a single array to implement three stacks. 

""" Java Solution """

""" 
public class ThreeStacks {
    public int capacity;
    public int numberStacks = 3;
    public int[] values;
    public int[] sizes; 
    
    //Constructor
    public ThreeStacks(int size){
        this.values = new int[size * numberStacks];
        this.sizes = new int[numberStacks];
        this.capacity = size; 
    }

    //Push values into the stack 
    public void push(int stackNum, int item) throws FullStackException{
        
        //If stack is full, throw a FullStackException
        if isFull(stackNum){
            throw new FullStackException(); 
        }

        //Add item to the stack
        sizes[stackNum]++; 
        values[indexAtTop(stackNum)] = item; 

    }

    //Remove the first value from the stack
    public int pop(int stackNumber) throws EmptyStackException {
        
        //If stack is empty, throw EmptyStackException 
        if isEmpty(stackNum){
            throw new EmptyStackException(); 
        }

        int item = values[indexAtTop(stackNum)];
        values[indexAtTop(stackNum)] = 0; 
        this.sizes[stackNum]--; 

        return item; 
    }

    //Return the top element of the stack
    public int peek(int stackNumber) throws EmptyStackException{
        //If stack is empty, throw EmptyStackException 
        if isEmpty(stackNum){
            throw new EmptyStackException(); 
        }

        //Return the top element 
        return values[indexAtTop(stackNum)]; 

    }

    //Return if the stack is empty
    public boolean isEmpty(int stackNumber){
        return sizes[stackNum] == 0; 
    }

    //Return if the stack is full
    public boolean isFull(int stackNumber){
        return sizes[stackNum] == capacity;
    }

    //Check the index at the top of the current stack
    private int indexAtTop(int stackNumber){
        int offset = stackNumber * this.numberStacks; 
        int currentSize = sizes[stackNumber]
        
        return offset + currentSize - 1; 
    }
}

"""

# 3.2 - Stack Min
# Design a stack which contains the function min() which returns the minimum element. 
# This is in addition to the push and pop functions. 
# Push, pop, and min functions should all operate in O(1) time. 

class StackMod: 
    def __init__(self): 
        self.stack = []
        self.minimum = []
    
    def push(self, item): 
        if (self.minimum[-1] == None) or (self.minimum[-1] > item): 
            self.minimum.append(item) 
            
        self.stack.append(item)

    def pop(self): 
        item = self.stack.pop()

        if (item == min()): 
            self.minimum.pop() 

        return item
    
    def peek(self): 
        return self.minimum[-1]

    def min(self):
        if (len(self.minimum) == 0): 
            return None

        return self.peek()

# 3.3 - Stack of Plates
# Imagine a (literal) stack of plates. If the stack is too high, it might topple. 
# The goal is to start a new stack when the previous stack exceeds some threshold. 
# This data structure, SetofStacks, should be composed of several stacks and should create a new stack once the previous one exceeds capacity. 
# The push() and pop() should behave identically to a single stack. 
# FOLLOW-UP: Implement a function popAt() which performs a pop operation on a specific substack.

class StackMod:
    def __init__(self, capacity): 
        self.stack = []
        self.capacity = capacity

        #These attributes are used to track the elements of stack for popAt() function
        self.top = None
        self.bottom = None
    
    def push(self, item):
        if not (self.isFull()):
            self.stack.append(item)
        
        #If the bottom stack is empty (i.e. empty stack)
        if (self.bottom == None):
            self.bottom = item
        self.top = item
    
    def pop(self):
        element = self.stack.pop()
        
        #Update the top element
        self.top = self.peek() 

        return element
    
    def popBottom(self): 
        element = self.stack.remove(0)

        #Update the bottom element
        self.bottom = self.stack[0] 

        return element
    
    def peek(self): 
        return self.stack[-1]
    
    def isEmpty(self): 
        return len(self.stack) == 0
    
    def isFull(self): 
        return len(self.stack) == self.capacity
    
    def size(self): 
        return len(self.stack)

class SetofStacks: 
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity
        
    def push(self, value):
        #Get the top-most available stack in the list of stacks
        lastStack = self._getLastStack()

        #If current stack is not full and not empty (i.e. has values in parameters), add value
        if not (lastStack.isFull()) and not (lastStack == None):
            lastStack.push(value)
        else: 
            #Otherwise add a new stack
            newStack = StackMod(self.capacity)
            newStack.push(value)
            self.stacks.append(newStack)

    def pop(self): 
        lastStack = self._getLastStack()

        if (not lastStack.isEmpty()):
            element = lastStack.pop()
        
        if (lastStack.isEmpty()): 
            self.stacks.remove(self.stacks[len(self.stacks) - 1])
        
        return element
    
    def popAt(self, index, removeTop = False): 
        #This assumes the index provided is zero-based
        stack = self.stacks[index]

        #Pop the element at the provided stack number
        if (removeTop): 
            element = stack.pop() 
        else: 
            element = stack.popBottom() 
        
        if (stack.isEmpty()): 
            self.stacks.remove(index) 
        elif (index + 1 < len(self.stacks)): 
            bottomElement = self.popAt(index + 1)
            stack.push(bottomElement)
        
        return element

    #Get the top-most available stack available
    def _getLastStack(self): 
        if len(self.stacks) == 0: 
            return None

        return self.stacks[len(self.stacks) - 1]
    
# 3.4 - Queue via Stacks
# Implement a MyQueue class which implements a queue using two stacks. 

class StackMod2:
    def __init__(self): 
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.remove(0)
    
    def peek(self): 
        return self.stack[0]
    
    def isEmpty(self): 
        return len(self.stack) == 0
    
    def isFull(self): 
        return len(self.stack) == self.capacity
    
    def size(self): 
        return len(self.stack)

#This class assumes this is not a priority queue
class MyQueue: 
    def __init__(self): 
        self.newStack = StackMod2()
        self.oldStack = StackMod2()
    
    def push(self, item): 
        #If the new stack is full, push the bottom element of the new stack to the old stack
        if (self.newStack.isFull()): 
            tempElement = self.newStack.pop()
            self.oldStack.push(tempElement) 
        
        self.newStack.push(item)
    
    def pop(self):
        #If there are elements in the old stack, remove elements from that one first
        if (self.newStack.isFull()) and not (self.oldStack.isEmpty()):
            return self.oldStack.pop()
        
        return self.newStack.pop() 

    #Check the next element that may be dequeued
    def peek(self):
        if (not self.oldStack.isEmpty()): 
            return self.oldStack.peek() 
        return self.newStack.peek() 

    def size(self): 
        return self.newStack.size() + self.oldStack.size()  

# 3.5 - Sort Stack
# Sort a stack such that the smallest items are on the top. 
# You can use an additional temporary stack, but you may not copy elements into any other data structure. 
# The stack supports the following operations: push, pop, peek, and isEmpty

class sortStack: 
    def __init__(self):
        self.stack = []
        self.tempStack = [] 
    
    def push(self, item): 
        #Check the items in order - note this solution requires O(N^2) time and O(N) space due to constraints of problem. 

        #If the intended element has a higher value than the top of stack, rearrange values to place in order
        if (item > self.stack.peek()):
            while (item > self.stack.peek()): 
                self.tempStack.append(self.stack.pop())
        
        #Add the intended element into the stack
        self.stack.append(item)

        #Return the elements from temporary stack back to the regular stack
        if (len(self.tempStack)): 
            while (len(self.tempStack) != 0):
                self.stack.append(self.tempStack.pop())

    def pop(self): 
        return self.stack.pop() 

    def peek(self): 
        return self.stack[-1]

    def isEmpty(self): 
        return (len(self.stack) == 0)

# 3.6 - Animal Shelter
# An animal shelter operate stritly "FIFO" basis for only dogs and cats. 
# People must adopt either the "oldest" (based on arrival time) of either animal, or adopt the oldest dog or cat. Adopters cannot specify an animal of other arrival times to their liking. 
# Create a data structure(s) to maintain this system and implement these operations: enqueue(), dequeueAny(), dequeueDog(), dequeueCat()
# You may use a built-in Linked List data structure.

class AnimalNode:
    def __init__(self, type):
        self.number = None
        self.type = type

        AnimalNode.PRIORITY_NUM += 1
    
    def getOrder(self): 
        return self.number
    
    def setOrder(self, number): 
        self.number = number

class AnimalQueue: 
    def __init__(self): 
        self.dogQueue = [] 
        self.catQueue = []
        self.order = 0 
    
    def enqueue(self, item): 
        self.item.setOrder(self.order)
        self.order += 1

        if (item.type == "dog"):
            self.dogQueue.append(item)
        elif (item.type == "cat"): 
            self.catQueue.append(item)
    
    def dequeueAny(self):
        #If either queue has no elements, return None
        if (len(self.dogQueue) == 0) and (len(self.catQueue) == 0): 
            return None

        if (len(self.dogQueue == 0)): 
            return self.dequeueCat()
        elif (len(self.catQueue == 0)): 
            return self.dequeueDog()

        #Check the priorty number of both queues, and compare the numbers to return earliest animal
        dog = self.dogQueue[0]
        cat = self.catQueue[0]

        if (dog.getOrder() < cat.getOrder()): 
            return self.dequeueDog()
        else: 
            return self.dequeueCat()
    
    def dequeueDog(self): 
        return self.dogQueue.remove(0)
    
    def dequeueCat(self): 
        return self.catQueue.remove(0)